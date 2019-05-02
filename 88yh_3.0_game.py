from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import random
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from telegram import Bot
import requests
import urllib3
import string
#机器人消息函数
def bot_function(message):
    bot = Bot(token="831458089:AAEi51QlG-kuNh4x8f_4H_3XaDYJKyyCIKI")
    bot.send_message(-284135974,message)

def http_code():
    urllib3.disable_warnings()
    r1 = requests.get('https://88yh686.com/#/',verify=False)
    code = r1.status_code  # 状态码
    normal_code = [100,101,200,201,202,203,204,205,206,300,302]
    message = 'https://88yh686.com/#/' + '异常报警：' + str(code)
    if code not in normal_code:
        bot_function(message)


error_message_list = ['Login failed, 48',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！(13670137)',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！',
                      'Login failed. undefined Error code: 48']

dr = webdriver.Chrome()
dr.implicitly_wait(30)
def new_check_error(flak):
    try:
        # # 判断是否有提示语
        WebDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]')))
        data = dr.find_element_by_xpath('/html/body/div[6]')
        error_message = data.get_attribute('textContent')
        result = str(error_message).find('维护')
        if error_message not in error_message_list and result == -1:
            return flak + 1
    except:
        try:
            WebDriverWait(dr, 5, poll_frequency=0.5).until(EC.alert_is_present())
            alert = dr.switch_to_alert()
            alert_message = (alert.text)
            if alert_message not in error_message_list:
                dr.switch_to_alert().accept()
                return flak + 1
            else:
                dr.switch_to_alert().accept()
                sleep(0.5)

        except:
            pass
#捕获异常
def check_error(game_name):
    try:
        # # 判断是否有提示语
        WebDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]')))
        data = dr.find_element_by_xpath('/html/body/div[6]')
        error_message = data.get_attribute('textContent')
        result = str(error_message).find('维护')
        message = ('88yh_PC错误提示：', game_name, error_message)     #'game_name 传参为需要打印预警的游戏名称'，例如VR彩票
        if error_message not in error_message_list and result == -1:
            bot_function(str(message))

    except:
        try:
            WebDriverWait(dr, 5, poll_frequency=0.5).until(EC.alert_is_present())
            alert_message = dr.switch_to_alert()
            error_message = (alert_message.text)
            if error_message in error_message_list:
                dr.switch_to_alert().accept()
                sleep(1)
            else:
                message = ('88yh_PC错误提示：', game_name, error_message)
                bot_function(str(message))
                dr.switch_to_alert().accept()
                sleep(1)
        except:
            pass
#递归判断游戏名称是否一致
def ele_check(i):
    sleep(0.5)
    new_ele = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[1]/h5').get_attribute('textContent')
    if i != new_ele:
        dr.find_element_by_class_name('wgic-search').click()
        sleep(2.5)
        ele_check(i)
dr.get('https://88yh188.com/#/')
dr.maximize_window()
sleep(0.5)
u"#-----------------------登录---------------------"
u'关闭首页公告'
try:
    WebDriverWait(dr,15,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div/div/span[1]')))
    news = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button')
    news.click()

except:
    pass
sleep(0.5)
#登录按钮
dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/span[1]').click()
sleep(0.3)
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input').send_keys('testbond06')
sleep(0.2)
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input').send_keys('123qwe')
sleep(0.2)
u'#点击登录'
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[3]/div/button').click()
WebDriverWait(dr,10,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[3]/div[5]/div/i')))
superrise = dr.find_element_by_xpath('//*[@id="app"]/div[3]/div[5]/div/i')
if superrise != None:
    superrise.click()

sleep(0.5)
WebDriverWait(dr,5,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/ul/li[7]')))
dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/ul/li[7]').click()
WebDriverWait(dr,5,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/button')))
dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/button').click()
handel = dr.window_handles
dr.switch_to_window(handel[1])
dr.implicitly_wait(30)
WebDriverWait(dr,15,poll_frequency=0.2).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/a')))
sleep(10)
#dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/a').click()
# 获取鼠标当前位置
pyautogui.position()
# 获取屏幕宽高度
x, y = pyautogui.size()
pyautogui.moveTo(965,578,duration=0.3)
pyautogui.click(965,578,duration=0.3)

# 点击允许加载flash
pyautogui.moveTo(312, 172, duration=0.3)
pyautogui.click(312, 172, duration=0.3)


sleep(6)
dr.close()
dr.switch_to_window(handel[0])
while True:
    u'进入个人中心'
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/h2').click()
    WebDriverWait(dr, 15, poll_frequency=0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[2]/ul/li[1]/a')))
    sleep(0.2)
    dr.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/ul/li[1]/a').click()
    sleep(0.3)
    WebDriverWait(dr, 20, poll_frequency=0.5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[1]/span')))

    sleep(1)
    u'获取当前时间'
    begin_time = datetime.datetime.now()
    center_tittle = {
        'Sun': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[1]/span',
        'AG': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[2]/span',
        'BBIN': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[3]/span',
        'LOTTO': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[4]/span',
        'PT': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[5]/span',
        'SB': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[6]/span',
        'VR': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[7]/span',
        'MG': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[8]/span',
        'KY': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[9]/span',
        'DS': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[10]/span',
        'HB': '//*[@id="app"]/div[2]/div/div[2]/div[3]/div[3]/ul/li[11]/span'
    }
    # i = 1
    # for i in range(1,5):
    for tittle in center_tittle:
        flak =0
        dr.find_element_by_xpath(center_tittle[tittle]).click()
        sleep(0.2)
        handel = dr.window_handles
        dr.switch_to_window(handel[1])
        all_num = new_check_error(flak)
        if  all_num == 1:
            dr.close()
            dr.switch_to_window(handel[0])
            dr.find_element_by_xpath(center_tittle[tittle]).click()
            sleep(0.2)
            handel = dr.window_handles
            dr.switch_to_window(handel[1])
            check_error(tittle)
        dr.close()
        dr.switch_to_window(handel[0])
        sleep(0.5)
    u'进入电子游戏'
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/ul/li[4]/a').click()
    WebDriverWait(dr, 20, poll_frequency=0.2).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[1]')))
    all_game = []
    for t in range(2,8):
        dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[1]/ul/li[' + str(t) + ']').click()
        sleep(1)
        WebDriverWait(dr,10,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[1]')))
        sleep(0.5)
        for i in range(1,6):
            element = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div['+ str(i) + ']/div[2]/div[1]/h5')
            game_name = element.get_attribute('textContent')
            all_game.append(game_name)
            sleep(0.3)
    #print(all_game)
    all_element = all_game
    dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[1]/ul/li[1]').click()
    sleep(2)
    for i in (all_element):
        flak = 0
        dr.find_element_by_class_name('input-search').send_keys(i)
        dr.find_element_by_class_name('wgic-search').click()
        sleep(2)
        ele_check(i)
        element = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]')
        ActionChains(dr).move_to_element(element).perform()
        dr.find_element_by_class_name('el-button').click()
        handel = dr.window_handles
        dr.switch_to_window(handel[1])
        elemerc = new_check_error(flak)
        if elemerc == 1:
            dr.close()
            dr.switch_to_window(handel[0])
            ActionChains(dr).move_to_element(element).perform()
            dr.find_element_by_class_name('el-button').click()
            handel = dr.window_handles
            dr.switch_to_window(handel[1])
            check_error(i)
        handel = dr.window_handles
        #print(len(handel))
        if len(handel) >1:
            dr.close()
        dr.switch_to_window(handel[0])
        sleep(0.5)
        u'发送ctrl + a 命令                                            '
        dr.find_element_by_class_name('input-search').send_keys(Keys.CONTROL, 'a')

        sleep(0.2)

    dr.find_element_by_class_name('input-search').send_keys(Keys.DELETE)
    sleep(0.8)
    Keys.HOME
    sleep(1)
    u'-------------logout-----------'
    logout = dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/h2')
    ActionChains(dr).move_to_element(logout).perform()
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div[2]/div/div/ul/li[6]').click()
    sleep(1)
    #http_code()
    u"#-----------------------登录---------------------"
    u'检测首页公告'
    try:
        WebDriverWait(dr, 15, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/span[1]')))
        news = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button')
        news.click()

    except:
        pass
    sleep(0.5)
    #登录按钮
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/span[1]').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input').send_keys('testbond06')
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input').send_keys('123qwe')
    sleep(0.5)
    u'#点击登录'
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[3]/div/button').click()
    WebDriverWait(dr, 15, poll_frequency=0.3).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div[5]/div/i')))
    superrise = dr.find_element_by_xpath('//*[@id="app"]/div[3]/div[5]/div/i')
    if superrise != None:
        superrise.click()
    sleep(1)










