# -*- coding: utf-8 -*-
# __author__ = 'corvin'

from __future__ import print_function

import os
import re
import json
import logging
import time
import vertica_python
from datetime import datetime
import sys
import requests

class VerticaConnHelper(object):

    @classmethod
    def get_connection(cls):
        conn_info = {
            # 'host': '172.16.1.195',
            'host': '47.91.170.6',
            'port': 5433,
            'user': 'corvin',
            'password': 'corvin123',
            'database': 'DB_MSDW',
            # 10 minutes timeout on queries
            'read_timeout': 600,
            # default throw error on invalid UTF-8 results
            'unicode_error': 'strict',
            # SSL is disabled by default
            'ssl': False,
            'connection_timeout': 60,
            # connection timeout is not enabled by default
            'ResultBufferSize': 0
        }
        # simple connection, with manual close
        connection = vertica_python.connect(**conn_info)
        return connection

class get_image_export(object):

    def __init__(self, table_name, output_path, date, logger=None):
        self.output_path = output_path
        self.table_name = table_name
        self.date = date
        self.logger = logger if logger else logging.getLogger()

    def create_table_if_notexists(self):
        try:
            connection = VerticaConnHelper.get_connection()
            cur = connection.cursor()
        except:
            cur.close()
            self.alert_message(": vertica_python 连接报错")
        table = self.table_name
        #advertiser_id, start_date, end_date, convert, active, show, campaign_id, stat_datetime, click, cost, register, pay_count
        sql = """CREATE TABLE {0} ( \
                                  video_path varchar(1500), \
                                  totalFrameNumber varchar(64), \
                                  frameRate varchar(64), \
                                  img_size varchar(64), \
                                  phash varchar(64), \
                                  insert_time datetime \
                                  ) \
                  order by video_path \
                  segmented by hash(video_path) all nodes;"""
        try:
            result = cur.execute("select * from {0};".format(table))
            cur.close()
            if result:
                return
        except vertica_python.errors.MissingRelation:
            cur.execute(sql.format(self.table_name))
            cur.close()
            return
        except vertica_python.errors.ConnectionError:
            self.create_table_if_notexists()
        except:
            self.alert_message(": vertica_python 建表连接报错")

    def batch_insert_records(self, table_name, records):
        logging.info(self.batch_insert_records)
        try:
            connection = VerticaConnHelper.get_connection()
            cur = connection.cursor()
        except:
            cur.close()
            self.alert_message(": vertica_python 插入连接报错")
        sql = """INSERT INTO {0} (video_path, totalFrameNumber, frameRate, img_size, phash, insert_time) \
                 VALUES (%s,%s,%s,%s,%s,%s); COMMIT;"""
        try:
            cur.executemany(sql.format(table_name), records)
            cur.close()
        except Exception as e:
            self.logger.error(str(e))
            self.alert_message(": vertica_python 连接报错")
        return

    def get_json_list(self,file_dir):
        '''传入file文件夹，获取文件名路径fileList'''
        fileList = [os.path.join(root, file) for root, dirs, files in os.walk(file_dir) for file in files if os.path.splitext(file)[1] == '.json' and re.findall('get_fb_fingerprint.'+str(self.date), file)]
        return fileList

    def run(self):
        # output_path = sys.argv[1]
        file_list = self.get_json_list(self.output_path)
        # connection = VerticaConnHelper.get_connection()
        table_name =self.table_name
        self.create_table_if_notexists()
        # params_list = ['advertiser_id', 'start_date', 'end_date','convert', 'active', 'show', 'campaign_id', 'click', 'cost', 'register', 'pay_count', 'stat_datetime']
        params_list = ["video_path", "totalFrameNumber", "frameRate", "img_size", "phash"]
        for file in file_list:
            records = []
            with open(file) as f:
                for line in f:
                    try:
                        obj = json.loads(line)
                    except:
                        continue
                    i_list = []
                    for param in params_list:
                        i = obj[param]
                        i_list.append(i)
                    insert_time = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                    i_list.append(insert_time)
                    # advertiser_id, start_date, end_date, convert, active, show, campaign_id, stat_datetime, click, cost, register, pay_count, insert_time
                    # print('*********************************************************')
                    # print(tuple(i_list))
                    # break
                    records.append(tuple(i_list))
                    if len(records) % 1000 == 0:
                        self.batch_insert_records(table_name, records)
                        # records = []
            if records:
                self.batch_insert_records(table_name,records)
        # time.sleep(10)
        # self.alert_message(": 电商分类信息爬取有太多失败,需要查看")

    def alert_message(self, ec_alert_message):

        sql1 = """
                  select * FROM {0};
               """
        connection = VerticaConnHelper.get_connection()
        cur = connection.cursor()
        try:
            after_data = cur.execute(sql1.format(self.table_name))
        except:
            cur.close()
            alert_url = "http://47.91.170.6:9999/v1/app?info={}".format(json.dumps(
                {
                    "app_id": 45,
                    "message": str(datetime.now().date()) + ' get_adgroup_export.py: vertica_python ConnectionError in export data',
                    "attachment": []
                }
            ))
            alert_res = requests.get(alert_url, timeout=60)
            logging.info('alert response: {}'.format(alert_res.content))
            return
        after_spider_count = 0
        for appid_list in cur.iterate():
            after_spider_count += 1
        cur.close()
        print("after_spider_count: {0}".format(after_spider_count))
        if after_spider_count > 50:
            alert_url = "http://47.91.170.6:9999/v1/app?info={}".format(json.dumps(
                {
                    "app_id": 45,
                    "message":str(datetime.now().date()) + ec_alert_message + " get_adgroup_export.py after_spider_count: {0}".format(after_spider_count),
                    "attachment": []
                }
            ))
            alert_res = requests.get(alert_url, timeout=60)
            logging.info('alert response: {}'.format(alert_res.content))
            sys.exit(1)
