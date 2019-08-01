#!/usr/bin/env bash
. /etc/profile

cur=`dirname $0; pwd`
cur=`cd $cur; pwd`
#export PYTHONPATH=`cd $cur/common_script; pwd`
export PYTHONPATH=`cd $cur; pwd`

if [ $# -lt 1 ]; then
    echo "sh run.sh time[yyyy-MM-dd]"
    exit 1
fi

time=$1

nohup  python $cur/script/fb_video_main.py $cur/data/fb_fingerprint/get_fb_fingerprint.$time.json $cur/data/fb_fingerprint   $time  $cur/data/fb_video  \
        > $cur/log/fbfingerprint_log/get_fb_fingerprint.$time.log 2>&1 &






