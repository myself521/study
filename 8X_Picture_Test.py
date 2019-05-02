from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import requests
from telegram import Bot
import os
import datetime

def bot_function(message):
    bot = Bot(token="623726932:AAFMZLjzWvY1wjQNtlTmWh-bue4jCUh7zMk")
    bot.send_message(-283638799,message)

dr = webdriver.Chrome()
dr.get('https://bax0511.com/html/category/photo/')
dr.maximize_window()
dr.implicitly_wait(30)
stat_time = datetime.datetime.now()
filea_path = './errro.txt'#检查本地异常记录文本是否存在
f = open(filea_path, 'w')
if os.path.exists(filea_path):
    f.truncate()
WebDriverWait(dr,timeout=15,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/ul/li[1]/div[1]/a/img')))
while True:
    element_list = dr.find_elements(By.CLASS_NAME, 'tc_nr')
    for element in element_list:
        name = dr.find_elements_by_class_name("t_p")
        sleep(0.2)
        #print(len(name))
        for i in range(1, len(name) + 1):
            picture_element = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[1]/a/img')
            name_element = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[2]/h3/a')
            title_name = name_element.get_attribute("textContent") #获取图组名称
            #获取图组缩略图链接
            title_url = picture_element.get_attribute('src')
            picture_element.click()
            handel = dr.window_handles
            dr.switch_to_window(handel[1])
            current_link = dr.current_url#获取当前浏览器窗口url地址
            picture_list = dr.find_elements_by_class_name('pc_ban')
            for pic in  picture_list:#获取当前页面的图片数量
                pi_link = dr.find_elements_by_xpath('//*[@id="image_show"]/img')
            for link in range(1,len(pi_link) + 1):#获取图片url
                img = dr.find_element(By.XPATH,'//*[@id="image_show"]/img[' + str(link) + str(']'))
                url = img.get_attribute('src')
                url_check = 'baxgood.com'#检测图片链接当中是否包含该域名
                if url_check not in url:
                    link_message = ('图片链接错误:',current_link,url)
                    with open(filea_path, 'a') as f:
                        f.write(str(link_message) + '\n')
                else:
                    re = requests.get(url)
                    code = re.status_code
                    if code != 200:
                        message = ('图片状态异常:',current_link,code,url)
                        with open(filea_path, 'a') as f:
                            f.write(str(message) + '\n')
            dr.close()
            sleep(0.3)
            dr.switch_to_window(handel[0])
        try:
            netx_page = dr.find_element_by_link_text('下一页')
            netx_page.click()
        except:

            end_time = datetime.datetime.now()
            print('程序总用时：',end_time - stat_time)
            dr.quit()

# Scheduler = BlockingScheduler()
# Scheduler.add_job(Test_8X_check,'interval',hours=24)
# Scheduler.start()

