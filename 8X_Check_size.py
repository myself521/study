from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
import datetime
dr = webdriver.Chrome()
title_Keyword = '380×235'#判断标题栏的尺寸数据
dr.get('https://bax0511.com/html/category/photo/')
size_path = './size_error.txt'
sz = open(size_path,'w')
if os.path.exists(size_path):
    sz.truncate()
dr.maximize_window()
dr.implicitly_wait(30)
start = datetime.datetime.now()
for cargoter in range(3,5):
    dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/ul/li[' + str(cargoter) + ']/a').click()
    while True:
        element_list = dr.find_elements(By.CLASS_NAME, 'tc_nr')
        for element in element_list:
            name = dr.find_elements_by_class_name("t_p")
            # print(len(name))
            for i in range(1, len(name) + 1):
                picture_element = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[1]/a/img')
                name_element = dr.find_element_by_xpath('/html/body/div[8]/div[2]/ul/li[' + str(i) + ']/div[2]/h3/a')
                title_name = name_element.get_attribute("textContent")
                # 获取
                title_url = picture_element.get_attribute('src')
                #print(title_url)
                dr.get(title_url)
                sleep(0.3)
                tit_name = dr.title
                print(title_url,tit_name)
                size_message = ('图片尺寸异常:',title_name,title_url)
                if title_Keyword not in tit_name:
                    with open(size_path,'a') as s:
                        s.write(str(size_message) + '\n')
                        s.close()
                        dr.back()
                        sleep(0.2)
                else:
                    dr.back()
                    sleep(0.2)
        try:
            next_page = dr.find_element_by_link_text('下一页')
            next_page.click()
        except:
            break
end = datetime.datetime.now()
print('程序总用时：',end - start)
dr.quit()


