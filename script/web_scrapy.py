# 2017年7月4日00:11:42
# silei
# 爬虫目标网站：http://www.yaoyanbaike.com/
# 获取信息BeautifulSoup+request

# -*- coding:UTF-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import sys
import codecs

if __name__ == "__main__":
    text_file_number = 0    # 同一类新闻下的索引数
    number = 1  # 同类别新闻不同页面下的索引数
    while (number <= 2):
        if number==1:   # 第一个新闻下地址是baby不是baby_数字所以要区分判断一下
            get_url = 'http://www.yaoyanbaike.com/category/baby.html'
        else:
            get_url = 'http://www.yaoyanbaike.com/category/baby_'+str(number)+'.html'   #这个是baby_数字，number就是目录索引数
        head = {}   #设置头
        head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        # 模拟浏览器模式，定制请求头
        download_req_get = request.Request(url = get_url, headers = head)
        # 设置Request
        download_response_get = request.urlopen(download_req_get)
        # 设置urlopen获取页面所有内容
        download_html_get = download_response_get.read().decode('UTF-8','ignore')
        # UTF-8模式读取获取的页面信息标签和内容
        soup_texts = BeautifulSoup(download_html_get, 'lxml')
        # BeautifulSoup读取页面html标签和内容的信息
        for link  in soup_texts.find_all(["a"]):
            print(str(text_file_number)+"   "+str(number)+"    "+link.get('href'))
            # 打印文件地址用于测试
            s=link.get('href')
            if s.find("/a/") == -1:
                print("错误网址")   # 只有包含"/a/"字符的才是有新闻的有效地址
            else:
                download_url = link.get('href')
                head = {}
                head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
                download_req = request.Request(url = "http://www.yaoyanbaike.com"+download_url, headers = head)
                print("http://www.yaoyanbaike.com"+download_url)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('UTF-8','ignore')
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all('article')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                p = re.compile("<[^>]+>")  
                text=p.sub("", str(soup_text))
                # 去除页面标签
                f1 = codecs.open('../data/baby/'+str(text_file_number)+'.txt','w','UTF-8')
                # 将信息存储在本地
                f1.write(text)
                f1.close()
                text_file_number = text_file_number + 1
        number = number + 1