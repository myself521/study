import requests
import re
import filecmp
import time
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

from telegram import Bot
#telegram机器人消息发送函数
def bot_function(a,message):
    bot = Bot(token="797169015:AAFV4OCUhrr3_QY1_aQjW1e7vX4W0rkjOgI")
    # -242222752为技术监控群
    #-288137810为机器人测试群
    bot.send_message(-288137810,a,message)#-242222752为技术监控群
import os
# def job():
while True:
    url_base_list = ['https://images.slaxc.com/app/api/x999_ios.js','https://images.slaxc.com/app/api/88yh_ios.js',
                     'https://images.slaxc.com/app/api/999y_ios.js','https://images.slaxc.com/app/api/77js_ios.js',
                     'https://images.slaxc.com/app/api/999h_ios.js']
    #print('begin')
    for url_base in url_base_list:
        time.sleep(1)
        html = requests.get(url_base)
        version = html.text
        link = re.findall(r'https://[a-zA-Z0-9.?/&_&-:]*',version)
        for li in link:
            time.sleep(1)
            message1 = requests.get(li).text
            filename1 = li.split("/")
            #print(filename1)
            fileame = filename1[len(filename1) - 1 ]
            #print(fileame)
            filepath = fileame + '.txt'
            f = open(filepath,'w')
            f.write(message1)
            f.close()
            if os.path.exists(filepath):
                new_filepath = fileame + 'a' + '.txt'
                f = open(new_filepath,'w')
                f.write(message1)
                f.close()
                result = filecmp.cmp(filepath,new_filepath)
                if result == True:
                    os.remove(new_filepath)
                else:
                    bot_function(new_filepath,'检测到手机版本异常，请及时处理')

# scheduler = BlockingScheduler()
# scheduler.add_job(job,'interval',seconds=300)
# scheduler.start()


