from selenium import webdriver
from time import sleep
import os
import re
import requests
import datetime

dr = webdriver.Chrome()
dr.get('https://npy37.com/')
dr.maximize_window()
dr.implicitly_wait(30)
stat_time = datetime.datetime.now()
def element_check():
    element = dr.find_element_by_link_text('大陆')
    if element == None:
        sleep(1)
        dr.refresh()
        element_check()
filea_path = './errro.txt'#检查本地异常记录文本是否存在
f = open(filea_path, 'w')
if os.path.exists(filea_path):
    f.truncate()
for category in range(2,8):
    categrory_name = dr.find_element_by_xpath('/html/body/header/div/ul/li['+ str(category) + ']/a')
    print(category)
    categrory_name.click()
    element_check()
    while True:
        video_elements = dr.find_elements_by_class_name('lb_zs')
        for videl in video_elements:
            video_url = dr.find_elements_by_class_name('col-lg-3')
        for i in range(1,len(video_url) + 1):
            video_element = dr.find_element_by_xpath('/html/body/section/div/div/div[2]/ul/li[' + str(i) + ']/div/div[1]/a/img')
            video_name = dr.find_element_by_xpath('/html/body/section/div/div/div[2]/ul/li[' + str(i) + ']/div/div[2]/h3/a').text
            video_element.click()
            element_check()
            new = dr.find_element_by_xpath('/html/body/section/div/div/script[2]').get_attribute('textContent')
            pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')# 匹配模式'(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            new_url = re.findall(pattern, new)
            new_url1 = str(new_url)
            url_keyword = new_url1[2:-12]
            res = requests.get(new_url[0])
            ts_error = ('TS文件缺少：', video_name)
            video_information = res.text#获取码率信息
            pn1 = re.compile('[\s\S]*?.ts')
            ts_list = re.findall(pn1, video_information)
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
                ts1_url = str(url_keyword)  + str(ts1)
                print(video_name,'ts_url:',ts1_url)
                re2 = requests.get(ts1_url)
                ts_status = re2.status_code
                error_message = ('TS链接状态异常:', video_name, ts1_url, ts_status)
                if ts_status != 200:
                    with open(filea_path, 'a') as f:
                        f.write(str(error_message) + '\n')
            dr.back()
            element_check()
        try:
            next_page = dr.find_element_by_link_text('下一页')
            next_page.click()
        except:
            break
end = datetime.datetime.now()
print('程序总用时：',end - stat_time)
dr.quit()
