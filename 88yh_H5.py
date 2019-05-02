from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from telegram import Bot
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
error_message_list = ['Login failed, 48',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！(13670137)',
                      '尊敬的客户您好，[BBIN平台]目前无可用余额，请至[会员中心]确认余额或入款以激活各项功能，谢谢您！',
                      'Login failed. undefined Error code: 48',
                      '维护中',
                      '网路异常,请重新开启游戏或检查连线状态! (13670139)',
                      '',
                      '临时维护中……',
                        '临时维护中',
                      '例行维护中（14：30—16:30）',
                      '\n\t\n\t\t\n\t\t\n\t\n',
                      '例行维护中']
des = {
    "platformName": "Android",
    #"deviceName": "HUAWEI MATE 9",
    "deviceName":"HUAWEI P20 Pro",
    "platformVersion": "8.1.0",
    "browserName": "Chrome",
    'unicodeKeyboard':True, #使用unicodeKeyboard的编码方式来发送字符串
    'resetKeyboard':True#将键盘给隐藏起来
}
#telegram机器人消息发送函数
def bot_function(message):
    bot = Bot(token="831458089:AAEi51QlG-kuNh4x8f_4H_3XaDYJKyyCIKI")
    # -242222752为技术监控群
    #-288137810为机器人测试群
    #-284135974为运营监控群（88yh）
    bot.send_message(-284135974,message)


dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
def ele_check(i):
    sleep(0.5)
    new_ele = dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/h3').get_attribute('textContent')
    if i != new_ele:
        dr.find_element_by_class_name('wgic-search').click()
        sleep(2.5)
        ele_check(i)
# 屏幕下滑方法
def screen_scroll():
    size = dr.get_window_size()
    js = "document.getElementsByClassName('scroll-container')[0].scrollTop = 1550"  # 1573为window_size height值
    dr.execute_script(js)


POLL_FREQUENCY = 0.5  # How long to sleep inbetween calls to the method
IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method


class WebAndroidDriverWait(object):
    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
        """Constructor, takes a WebDriver instance and timeout in seconds.

           :Args:
            - driver - Instance of WebDriver (Ie, Firefox, Chrome or Remote)
            - timeout - Number of seconds before timing out
            - poll_frequency - sleep interval between calls
              By default, it is 0.5 second.
            - ignored_exceptions - iterable structure of exception classes ignored during calls.
              By default, it contains NoSuchElementException only.

           Example:
            from selenium.webdriver.support.ui import WebAndroidDriverWait \n
            element = WebAndroidDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebAndroidDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
        """
        self._driver = driver
        self._timeout = timeout
        self._poll = poll_frequency
        # avoid the divide by zero
        if self._poll == 0:
            self._poll = POLL_FREQUENCY
        exceptions = list(IGNORED_EXCEPTIONS)
        if ignored_exceptions is not None:
            try:
                exceptions.extend(iter(ignored_exceptions))
            except TypeError:  # ignored_exceptions is not iterable
                exceptions.append(ignored_exceptions)
        self._ignored_exceptions = tuple(exceptions)

    def __repr__(self):
        return '<{0.__module__}.{0.__name__} (session="{1}")>'.format(
            type(self), self._driver.session_id)

    def until(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)

    def until_not(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is False."""
        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if not value:
                    return value
            except self._ignored_exceptions:
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message)

#捕获异常函数
def check_error(game_name):
    try:
        # # 判断是否有提示语
        WebAndroidDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]')))
        data = dr.find_element_by_xpath('/html/body/div[6]')
        error_message = data.get_attribute('textContent')
        message = ('88yh_H5错误提示：', game_name, error_message)     #'game_name 传参为需要打印预警的游戏名称'，例如VR彩票
        result = str(error_message).find('维护')
        if error_message not in error_message_list and result == -1:
            bot_function(str(message))
    except:
        try:
            WebAndroidDriverWait(dr, 10, poll_frequency=0.5).until(EC.alert_is_present())
            alert_message = dr.switch_to_alert()
            error_message = (alert_message.text)
            if error_message in error_message_list:
                dr.switch_to_alert().accept()
                sleep(1)
            else:
                message = ('88yh_H5错误提示：', game_name, alert_message.text)
                bot_function(str(message))
                dr.switch_to_alert().accept()
                sleep(1)
        except:
            pass

def new_check_error(flak):
    try:
        # # 判断是否有提示语
        WebAndroidDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]')))
        data = dr.find_element_by_xpath('/html/body/div[6]')
        error_message = data.get_attribute('textContent')
        result = str(error_message).find('维护')
        if error_message not in error_message_list and result == -1:
            return flak + 1

    except:
        try:
            WebAndroidDriverWait(dr, 5, poll_frequency=0.5).until(EC.alert_is_present())
            alert_message = dr.switch_to_alert()
            error_message = (alert_message.text)
            if error_message not in error_message_list:
                dr.switch_to_alert().accept()
                sleep(1)
                return flak + 1
            else:
                dr.switch_to_alert().accept()
                sleep(1)
        except:
            pass

#元素坐标进行点击操作函数
def element_action(start_ele,end_ele,game_name_start,game_name_end):
    element_list = dr.find_elements(By.CLASS_NAME, 'scroll-container')
    for element in element_list:
        name = dr.find_elements_by_class_name("game_item")
        sleep(0.5)
    for i in range(1, len(name)):
        flak = 0
        game_element = dr.find_element_by_xpath(start_ele + str(i) + end_ele)
        name_element = dr.find_element_by_xpath(game_name_start + str(i) + game_name_end)
        game_name = name_element.get_attribute('textContent')
        game_element.click()
        handel = dr.window_handles
        dr.switch_to.window(handel[1])
        new_flak = new_check_error(flak)
        if new_flak == 1:
            dr.close()
            dr.switch_to_window(handel[0])
            game_element.click()
            handel = dr.window_handles
            dr.switch_to.window(handel[1])
            check_error(game_name)
        dr.close()
        dr.switch_to.window(handel[0])
        sleep(1)
    dr.find_element_by_class_name('active').click()
    sleep(0.5)

dr.get('https://88yh188.com/m/#/')
dr.hide_keyboard()
sleep(10)
try:
    WebAndroidDriverWait(dr, 30, poll_frequency=0.3).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div/div[2]/div[1]')))
    news = dr.find_element_by_xpath('/html/body/div[11]/div/div[2]/div[1]')
    news.click()
except:
    pass
sleep(0.5)
u'登录操作'
dr.find_element_by_xpath('//*[@id="app"]/div[2]/div/ul/li[5]/a').click()
WebAndroidDriverWait(dr,10,poll_frequency=0.2).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[7]/div/div/div/div[1]/div[1]/input')))
dr.find_element_by_xpath('/html/body/div[7]/div/div/div/div[1]/div[1]/input').send_keys('testbond05')
dr.find_element_by_xpath('/html/body/div[7]/div/div/div/div[1]/div[2]/input').send_keys('123qwe')
#dr.hide_keyboard()
sleep(0.5)
dr.find_element_by_class_name('weui-btn').click()
WebAndroidDriverWait(dr,20,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[4]/div/i')))
dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/i').click()
sleep(0.5)
while True:
    screen_scroll()
    sleep(1)
    u'电子游戏'
    dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[2]').click()
    WebAndroidDriverWait(dr,10,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[1]')))
    sleep(2)
    game_list = dr.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]')
    #print(game_list)
    sleep(1)
    for game in game_list:
        name = dr.find_elements_by_class_name('game_item')
        sleep(0.1)
    #print(len(name))
    all_game = []
    for i in range(1,len(name)):
        element = dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div['+str(i)+']/div/div[2]/h3')
        game_name = element.get_attribute('textContent')
        all_game.append(game_name)
    #print(all_game)
    all_element = all_game
    for ele in all_element:
        flak = 0
        u'根据游戏名字进行循环搜索'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/input').send_keys(ele)
        dr.find_element_by_class_name('wgic-search').click()
        sleep(2)
        element1 = dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
        ele_check(ele)
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
        handel = dr.window_handles
        dr.switch_to.window(handel[1])
        elemrc = new_check_error(flak)
        if elemrc == 1:
            dr.close()
            dr.switch_to_window(handel[0])
            dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div/div[1]').click()
            handel = dr.window_handles
            dr.switch_to.window(handel[1])
            check_error(ele)
        dr.close()
        dr.switch_to.window(handel[0])
        sleep(0.5)
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/input').send_keys(Keys.CONTROL, 'a')
        sleep(0.2)
    sleep(1)
    try:
        dr.find_element_by_class_name('btnx').click()
        WebAndroidDriverWait(dr,10,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div[8]/div/div[1]')))
    except:
        dr.find_element_by_class_name('btnx').click()
        WebAndroidDriverWait(dr, 10, poll_frequency=0.3).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div[8]/div/div[1]')))
    dr.find_element_by_class_name('left').click()
    sleep(0.5)
    i =1
    for i in range(1,2):
        screen_scroll()
        sleep(1)
        u'真人'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[1]').click()

        WebAndroidDriverWait(dr,15,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div/div[1]/div/div[1]')))
        sleep(1.5)
        element_action('//*[@id="app"]/div[1]/div/div[2]/div/div/div[', ']/div/div[1]',
                   '//*[@id="app"]/div[1]/div/div[2]/div/div/div[', ']/div/div[2]/h3')
        sleep(0.5)
        screen_scroll()
        sleep(1)
        u'彩票'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[3]').click()
        WebAndroidDriverWait(dr,10,poll_frequency=0.3).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="html"]/div/div[2]/div[1]/div/div[1]')))
        element_action('//*[@id="html"]/div/div[2]/div[',
                       ']/div/div[1]','//*[@id="html"]/div/div[2]/div[',']/div/div[2]/h3')
        sleep(0.5)
        screen_scroll()
        sleep(1)
        u'棋牌'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[4]').click()
        WebAndroidDriverWait(dr,10,poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[1]')))
        element_action('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div/div[',']/div/div[1]','//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div/div[',']/div/div[2]/h3')
        sleep(0.5)
        screen_scroll()
        sleep(1)
        u'体育'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[5]').click()
        WebAndroidDriverWait(dr,10,poll_frequency=1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="html"]/div/div/div[2]/div[1]/div/div[2]/button')))
        element_list = dr.find_elements(By.CLASS_NAME, 'scroll-container')
        for element in element_list:
            name = dr.find_elements_by_class_name("game_item")
            sleep(0.5)
        for i in range(1, len(name) + 1):
            flak = 0
            game_element = dr.find_element_by_xpath('//*[@id="html"]/div/div/div[2]/div[' + str(i) + ']/div/div[1]')
            name_element = dr.find_element_by_xpath('//*[@id="html"]/div/div/div[2]/div[' + str(i) + ']/div/div[2]/h3')
            game_name = name_element.get_attribute('textContent')
            game_element.click()
            handel = dr.window_handles
            dr.switch_to.window(handel[1])
            new_check_error(flak)
            if flak == 1:
                dr.close()
                dr.switch_to_window(handel[0])
                game_element.click()
                handel = dr.window_handles
                dr.switch_to.window(handel[1])
                check_error(game_name)
            dr.close()
            dr.switch_to.window(handel[0])
            sleep(1)
        dr.find_element_by_class_name('active').click()
        sleep(0.5)
        screen_scroll()
        sleep(1)
        u'捕鱼'
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[2]/div/div[4]/div[4]/div[6]').click()
        WebAndroidDriverWait(dr,10,poll_frequency=0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div/div/div[1]')))
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div/div/div[1]').click()
        handel = dr.window_handles
        dr.switch_to_window(handel[1])
        check_error('AG捕鱼')
        dr.close()
        handel = dr.window_handles
        dr.switch_to_window(handel[0])
        dr.find_element_by_class_name('active').click()
        sleep(0.5)
    u'退出登录'
    dr.find_element_by_class_name('wgic-user-b').click()
    size = dr.get_window_size()
    js = "document.getElementsByClassName('scroll-container')[0].scrollTop = 1650"  # 1573为window_size height值
    dr.execute_script(js)
    WebAndroidDriverWait(dr,15,poll_frequency=0.5).until(EC.visibility_of_element_located((By.CLASS_NAME,'weui-btn')))
    dr.find_element_by_class_name('weui-btn').click()
    sleep(1)
    u'关闭首页公告'
    try:
        WebAndroidDriverWait(dr, 10, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div/div/span[1]')))
        news = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[3]/div/div[1]/button')
        news.click()

    except:
        pass
    u'登录操作'
    dr.find_element_by_xpath('//*[@id="app"]/div[2]/div/ul/li[5]/a').click()
    WebAndroidDriverWait(dr, 15, poll_frequency=0.2).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div/div/div[1]/div[1]/input')))
    dr.find_element_by_xpath('/html/body/div[7]/div/div/div/div[1]/div[1]/input').send_keys('testbond05')
    sleep(0.2)
    dr.find_element_by_xpath('/html/body/div[7]/div/div/div/div[1]/div[2]/input').send_keys('123qwe')
    sleep(0.5)
    dr.find_element_by_class_name('weui-btn').click()
    try:
        WebAndroidDriverWait(dr, 20, poll_frequency=0.5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[4]/div/i')))
        dr.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[4]/div/i').click()
    except:
        pass
    sleep(0.5)
