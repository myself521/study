#picture_spider
# -*- coding: utf-8 -*-
import requests, os
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time

headers = {'Referer': 'https://www.baidu.com/link?url=9e1kI-jXcP9uVuQcw0htp_58IUPdjOC6D3KLW3cA28o-Mjcdabu8P_RP7dLgLEBN&wd=&eqid=ffc86cfd000253bd000000035a2bfb30',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

def get_picture_url(url):
    url_lists = []

    req = requests.get(url, headers=headers)
    #time.sleep(3)
    soup = BeautifulSoup(req.text, 'html.parser')
    content_info = soup.find('dl', {'class': 'list-left'})
    div_info = content_info.find_all('a')
    print("print div_info\n",div_info)
    for list in div_info:
        url_list = list.get('href')
        url_lists.append(url_list)
#    print(url_lists)
    return url_lists

def download_picture(url):
    req = requests.get(url, headers=headers)
    #print(req.encoding)
    req.encoding = 'gb2312'
    soup = BeautifulSoup(req.text, 'html.parser')
    content_info = soup.find('div', {'class': 'content'})
    #print("打印conten_info",content_info)
    img_info = content_info.find('img')
    name = img_info.get('alt')[:-4]
    print("打印图组名字：",name)
    src = img_info.get('src')[:-5]
    #print("print src \n",src)
    max_page = content_info.find('div',{'class':'content-page'}).contents[0].get_text()[1:-1]
    print("打印当前图组最大页数：",max_page)
    #breakpoint()

    path = mkdir_name(name)
    for i in range(int(max_page)):
        n = i + 1
        time.sleep(1)
        url = src + str(n) + '.jpg'
        req = requests.get(url, headers=headers, timeout=500)
        filepath = path + '/' + str(n) + '.jpg'
        if os.path.exists(filepath):
            print('exists:', filepath)
            continue
        with open(filepath, 'wb') as f:
            f.write(req.content)
        print('end download', url)

def mkdir_name(name):
    path = './data/' + name
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    return path

if __name__ == '__main__':
    start = time.time()
    url = 'http://www.mm131.com/xinggan/'
    for n in range(5,10):#从第五页开始抓取  5 至第十页结束（不包含第十页）
        start = time.time()
        url = 'http://www.mm131.com/xinggan/'
        print("准备开始抓取为%d页的数据"%n)
        url = url + 'list_6_'+ str(n)+'.html'
        print(url)
        #breakpoint()
        url_lists1 = get_picture_url(url)
        url_lists = list(set(url_lists1))#对列表内的数据去重操作
        print("第%d页的图组链接列表" %n,url_lists)
        p = Pool(4)#线程数设置
        for url in url_lists:
            p.apply_async(download_picture, (url,))
        p.close()
        p.join()
        print('第%d页下载完成')
        end = time.time()
        print("第%d页下载耗时" %n,end - start)
        time.sleep(5)
    else:
          print("-----所有数据都已经下载完成-------")

