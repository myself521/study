from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import os
import re
import requests
import datetime
url_keword = 'https://jiuktp.com/v/'
header = {'channel': '0',
          'Accept': 'application/json, text/javascript, */*; q=0.01',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

dr = webdriver.Chrome()
dr.get('https://bax0519.com/html/category/video/')
title_Keyword = '380×235'#判断标题栏的尺寸数据

def picture_size(url,name,filepath):
    dr.get(url)
    sleep(3)
    tit_name = dr.title
    print(url, tit_name)
    size_message = ('图片尺寸异常:', name, url)
    if title_Keyword not in tit_name:
        with open(filepath, 'a') as s:
            s.write(str(size_message) + '\n')
            s.close()
            dr.back()
            sleep(1)
    else:
        dr.back()
        sleep(1)
dr.maximize_window()
dr.implicitly_wait(30)
stat_time = datetime.datetime.now()
def element_check():
    element = dr.find_element_by_link_text('视频')
    if element == None:
        sleep(1)
        dr.refresh()
        element_check()
filea_path = './errro.txt'#检查本地异常记录文本是否存在
f = open(filea_path, 'w')
if os.path.exists(filea_path):
    f.truncate()
while True:
    video_elements = dr.find_elements_by_class_name('tc_nr')
    for videl in video_elements:
        video_url = dr.find_elements_by_class_name('t_p')
    for i in range(1,len(video_url) + 1):
        video_element = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[1]/a/img')
        video_name = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[2]/h3/a').text
        video_element.click()
        handel = dr.window_handles
        dr.switch_to_window(handel[1])
        element_check()
        md5 = dr.find_element_by_xpath('//*[@id="vpath"]').get_attribute('textContent')
        md6 = md5[:-10]
        #print(md6)
        new_url  = str(url_keword) + str(md5)
        #print(new_url)
        res = requests.get(new_url)
        video_information = res.text#获取码率信息
        if 'ts' not in video_information:
            pn = re.compile('[\s\S]*?.m3u8')
            items = re.findall(pn,video_information)#将码率字符串转换为列表数据
            for it in items:
                it1 = it[-9:]
                ts_url = str(url_keword) +str(md6) + str(it1)
                retr = requests.get(ts_url)
                ts_information = retr.text
                pn1 = re.compile('[\s\S]*?.ts')
                ts_list = re.findall(pn1,ts_information)
                ts_error = ('TS文件缺少：',video_name,md6)
                c = 0
                for ts in ts_list:
                    ts0 = ts[-13:]
                    ts3 = ts[-13:-8]
                    d = int(ts3)
                    if d == c:
                        c += 1
                    else:
                        with open(filea_path, 'a') as f:
                            f.write(str(ts_error) + '\n')
                    ts1_url = str(url_keword) + str(md6) + str(ts0)
                    re2 = requests.get(ts1_url)
                    ts_status = re2.status_code
                    error_message = ('TS链接状态异常:', video_name, ts1_url,ts_status)
                    if ts_status != 200:
                        with open(filea_path,'a') as f:
                            f.write(str(error_message) + '\n')
        else:
            pn1 = re.compile('[\s\S]*?.ts')
            ts_list = re.findall(pn1, video_information)
            #print('this ts_list', ts_list)
            a = 0
            for ts in ts_list:
                ts1 = ts[-8:]
                ts2 = ts[-8:-3]
                b = int(ts2)
                if b == a:
                    a += 1
                else:
                    with open(filea_path,'a') as f:
                        f.write(str(ts_error) + '\n')
                ts1_url = str(url_keword) + str(md6) + str(ts1)
                re2 = requests.get(ts1_url)
                ts_status = re2.status_code
                error_message = ('TS链接状态异常:', video_name, ts1_url, ts_status)
                if ts_status != 200:
                    with open(filea_path, 'a') as f:
                        f.write(str(error_message) + '\n')
        dr.close()
        dr.switch_to_window(handel[0])
    try:
        next_page = dr.find_element_by_link_text('下一页')
        next_page.click()
    except:
        end = datetime.datetime.now()
        print('程序总用时：',end - stat_time)
        dr.quit()
