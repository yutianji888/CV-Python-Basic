# -*- coding: utf-8 -*-
# __author__ = 'corvin'

import vertica_python
import logging
import requests
from datetime import datetime
import json
import sys
import re
import pandas as pd

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

class get_linklist_vertica(object):

    def __init__(self, table_name):
        self.table_name = table_name

    def create_table_if_notexists(self, table_name):
        try:
            connection = VerticaConnHelper.get_connection()
            cur = connection.cursor()
        except:
            cur.close()
            self.alert_message(": vertica_python 插入连接报错")
        table = table_name
        #['category0_en', 'category1_en', 'category2_en', 'category3_en','category4_en', 'category5_en', 'category0_cn', 'category1_cn',
        #'category2_cn', 'category3_cn', 'category4_cn', 'category5_cn','category_list']
        sql = """CREATE TABLE {0} ( \
                                  cf_reference_detail varchar(1500), \
                                  video_url varchar(2000), \
                                  totalFrameNumber varchar(64), \
                                  frameRate varchar(64), \
                                  img_size varchar(64), \
                                  phash varchar(64), \
                                  insert_time datetime \
                                  ) \
                  order by cf_reference_detail \
                  segmented by hash(cf_reference_detail) all nodes;"""
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

    def get_linklist(self):
        # sql = """
        #         select t.cf_reference_detail from cmf.cmf_creative_files t where t.cf_reference_detail like '%.mp4%' limit 20;
        #       """
        sql = """
            select t.cf_reference_detail from cmf.cmf_creative_files t 
            where t.cf_reference_detail like '%.mp4%' or t.cf_reference_detail like '%.mov%' or t.cf_reference_detail like '%.avi%' 
            and NOT EXISTS
            (select a.cf_reference_detail from datamining.dmn_cmf_video_fingerprint a GROUP BY a.cf_reference_detail) 
            group by t.cf_reference_detail;
        """
        try:
            connection = VerticaConnHelper.get_connection()
            cur = connection.cursor()
        # except vertica_python.errors.ConnectionError:
        #     cur.close()
        #     self.get_linklist()
        except:
            # cur.close()
            alert_url = "http://47.91.170.6:9999/v1/app?info={}".format(json.dumps(
                {
                    "app_id": 45,
                    "message": str(datetime.now().date()) + ": vertica_python连接报错",
                    "attachment": []
                }
            ))
            alert_res = requests.get(alert_url, timeout=60)
            logging.info('alert response: {}'.format(alert_res.content))
        self.create_table_if_notexists(self.table_name)
        # data = cur.execute(sql.format(self.table_name))
        data = cur.execute(sql)
        id_list = [row[0] for row in cur.iterate()]
        cur.close()
        id_list = list(set(id_list))
        return id_list

    def alert_message(self, ec_alert_message):

        sql1 = """
                  SELECT count(1) from datamining.dmn_cmf_video_fingerprint; 
                """
        connection = VerticaConnHelper.get_connection()
        cur = connection.cursor()
        try:
            after_data = cur.execute(sql1)
        except:
            cur.close()
            alert_url = "http://47.91.170.6:9999/v1/app?info={}".format(json.dumps(
                {
                    "app_id": 45,
                    "message": str(datetime.now().date()) + ' reports_get_advertiser.py: vertica_python ConnectionError in export data',
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
                    "message": str(datetime.now().date()) + ec_alert_message + " reports_get_advertiser.py after_spider_count: {0}".format(
                        after_spider_count),
                    "attachment": []
                }
            ))
            alert_res = requests.get(alert_url, timeout=60)
            logging.info('alert response: {}'.format(alert_res.content))
            sys.exit(1)
