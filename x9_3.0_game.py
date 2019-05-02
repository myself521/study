from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from telegram import Bot
import requests
import urllib3
import string
#机器人消息函数
def bot_function(message):
    bot = Bot(token="797169015:AAFV4OCUhrr3_QY1_aQjW1e7vX4W0rkjOgI")
    bot.send_message(-340121886,message)
def http_code():
    urllib3.disable_warnings()
    r1 = requests.get('https://x999.club/#/',verify=False)
    code = r1.status_code  # 状态码
    normal_code = [100,101,200,201,202,203,204,205,206,300,302]
    message = 'https://x999.club/#/' + '异常报警：' + str(code)
    if code not in normal_code:
        bot_function(message)


error_message_list = ['Login failed, 48',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！(13670137)',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！',
                      'Login failed. undefined Error code: 48']

dr = webdriver.Chrome()
dr.implicitly_wait(30)
#捕获异常
def check_error(game_name):
    try:
        # # 判断是否有提示语
        WebDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]')))
        data = dr.find_element_by_xpath('/html/body/div[6]')
        error_message = data.get_attribute('textContent')
        result = str(error_message).find('维护')
        message = ('X9_PC错误提示：', game_name, error_message)     #'game_name 传参为需要打印预警的游戏名称'，例如VR彩票
        if error_message not in error_message_list and result == -1:
            bot_function(str(message))
    except:
        try:
            WebDriverWait(dr, 10, poll_frequency=0.5).until(EC.alert_is_present())
            alert_message = dr.switch_to_alert()
            error_message = (alert_message.text)
            if error_message in error_message_list:
                dr.switch_to_alert().accept()
            else:
                message = ('X9_PC错误提示：', game_name, error_message)
                bot_function(str(message))
                dr.switch_to_alert().accept()
        except:
            pass
def ele_check(i):
    sleep(0.3)
    new_ele = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[1]/h5').get_attribute('textContent')
    #print(i,new_ele)
    if i != new_ele:
        dr.find_element_by_class_name('wgic-search').click()
        ele_check(i)
dr.get('https://x999.club/#/')
dr.maximize_window()
sleep(0.5)
u"#-----------------------登录---------------------"
try:
    u'关闭首页公告'
    WebDriverWait(dr,1,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button/i')))
    news = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button/i')
    if news == None:
        pass
    else:
        news.click()
except:
    pass
sleep(0.5)
#登录按钮
dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div/div/span[1]').click()
sleep(0.3)
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input').send_keys('testbond06')
sleep(0.2)
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input').send_keys('123qwe')
sleep(0.2)
u'#点击登录'
dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[3]/div/button').click()
WebDriverWait(dr,10,poll_frequency=0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'user-oper')))
sleep(0.5)
dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/ul/li[4]/a').click()
WebDriverWait(dr,15,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/button')))
dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/button').click()
handel = dr.window_handles
dr.switch_to_window(handel[1])
WebDriverWait(dr,10,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/a')))
sleep(0.5)
x, y = pyautogui.size()
pyautogui.moveTo(965,578,duration=0.2)
pyautogui.click(965,578,duration=0.2)
sleep(1)
# 获取鼠标当前位置
pyautogui.position()
# 点击允许加载flash
pyautogui.moveTo(312, 172, duration=0.2)
pyautogui.click(312, 172, duration=0.2)
sleep(5)
dr.close()
dr.switch_to_window(handel[0])
while True:
    u'进入个人中心'
    dr.find_element_by_class_name('user-oper').click()
    WebDriverWait(dr,10,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/span')))
    center_tittle = {
        'AG': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[1]/span',
        'BBIN': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[2]/span',
        'LOTTO': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[3]/span',
        'PT': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[4]/span',
        'SB': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[5]/span',
        'VR': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[6]/span',
        'MG': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[7]/span',
        'KY': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[8]/span',
        'Sun':'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[9]/span',
        'DS': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[10]/span',
        'LMG':'//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[11]/span',
        'HB': '//*[@id="app"]/div[2]/div/div[2]/div[2]/div[3]/ul/li[12]/span'
    }
    # i = 1
    # for i in range(1,5):
    for tittle in center_tittle:
        dr.find_element_by_xpath(center_tittle[tittle]).click()
        sleep(0.2)
        handel = dr.window_handles
        dr.switch_to.window(handel[1])
        check_error(tittle)
        dr.close()
        dr.switch_to.window(handel[0])
        sleep(0.3)
    u'进入电子游戏'
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/ul/li[5]/a').click()
    WebDriverWait(dr, 20, poll_frequency=0.2).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[1]')))
    all_game = []
    for t in range(2,8):
        dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[1]/ul/li[' + str(t) + ']').click()
        sleep(0.5)
        WebDriverWait(dr,10,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[1]')))
        sleep(0.5)
        for i in range(1,4):
            element = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div['+str(i)+']/div[2]/div[1]/h5')
            game_name = element.get_attribute('textContent')
            all_game.append(game_name)
            sleep(0.3)
    #print(all_game)
    all_element = all_game
    dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[4]/div[1]/ul/li[1]').click()
    sleep(2)
    for i in all_element:
        dr.find_element_by_class_name('input-search').send_keys(i)
        dr.find_element_by_class_name('wgic-search').click()
        sleep(2)
        element = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[5]/div[1]/div[1]')
        if element == None:
            continue
        ele_check(i)
        ActionChains(dr).move_to_element(element).perform()
        sleep(0.1)
        dr.find_element_by_class_name('el-button').click()
        handel = dr.window_handles
        dr.switch_to.window(handel[1])
        check_error(i)
        dr.close()
        dr.switch_to.window(handel[0])
        sleep(0.1)
        u'发送ctrl + a 命令                                            '
        dr.find_element_by_class_name('input-search').send_keys(Keys.CONTROL, 'a')
        sleep(0.2)

    dr.find_element_by_class_name('input-search').send_keys(Keys.BACK_SPACE)
    sleep(1)
    Keys.HOME
    sleep(0.5)
    u'-------------logout-----------'
    logout = dr.find_element_by_class_name('user-oper')
    ActionChains(dr).move_to_element(logout).perform()
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div/div[2]/div[2]/ul/li[6]/a').click()
    sleep(1)
    #http_code()
    u"#-----------------------登录---------------------"
    try:
        u'关闭首页公告'
        WebDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/span[1]')))
        news = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button')
        if news == None:
            pass
        else:
            news.click()
    except:
        pass
    sleep(0.5)

    #登录按钮
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div/div/span[1]').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[1]/div/div/input').send_keys('testbond06')
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[2]/div/div/input').send_keys('123qwe')
    sleep(0.5)
    u'#点击登录'
    dr.find_element_by_xpath('//*[@id="pane-0"]/form/div[3]/div/button').click()
    WebDriverWait(dr, 15, poll_frequency=0.3).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'user-oper')))
    sleep(0.5)









