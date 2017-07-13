# 2017年7月13日15:27:02
# silei
# 爬虫目标网站：http://www.thepaper.cn/newsDetail_forward_
# 获取信息BeautifulSoup+request
# 正确新闻的爬去，分词，去停用词

# -*- coding:UTF-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import sys
import codecs
import jieba
import requests

if __name__ == "__main__":   
    text_file_number = 0
    web_url_number = 1701736
    while web_url_number < 1731414 :
        get_url = 'http://www.thepaper.cn/newsDetail_forward_'+str(web_url_number)   
        head = {}   #设置头
        head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        # 模拟浏览器模式，定制请求头
        download_req_get = request.Request(url = get_url, headers = head)
        # 设置Request
        r = requests.get(get_url)
        print(get_url)
        print(r.status_code)
        download_response_get = request.urlopen(download_req_get)
        # 设置urlopen获取页面所有内容
        download_html_get = download_response_get.read().decode('UTF-8','ignore')
        # UTF-8模式读取获取的页面信息标签和内容
        soup_text = BeautifulSoup(download_html_get, 'lxml')
        soup_text.find_all(["news_txt"])
        # BeautifulSoup读取页面html标签和内容的信息
        web_text = re.compile("<[^>]+>")
        content=web_text.sub("", str(soup_text))
        if soup_text == "" :
        	print('字符串为空')
        	continue
        # 去除页面标签
        stoplist = {}.fromkeys([content.strip() for content in open("../data/stopword.txt",encoding= 'UTF-8') ])  
        # 读取停用词在列表中
        seg_list = jieba.lcut(content,cut_all=False)
        # jieba分词精确模式
        seg_list = [word for word in list(seg_list) if word not in stoplist]  
        # 去除停用词
        # print("Default Mode:", "/ ".join(seg_list))
        file_write = codecs.open('../data/train_data_news/true/'+str(text_file_number)+'.txt','w','UTF-8')
        # 将信息存储在本地
        for i in range(len(seg_list)):
            file_write.write(str(seg_list[i])+'\n')
        file_write.close()
        print('写入成功')
        text_file_number = text_file_number + 1
        web_url_number = web_url_number + 1