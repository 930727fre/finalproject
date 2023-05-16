import lxml, requests, time, json, datetime, re
from bs4 import BeautifulSoup as bs

def LeetCode():
    url="https://leetcode.com/contest/"
    response=requests.get(url)
    requestsTry=5
    while(not response.ok and requestsTry>0):
        time.sleep(1)
        response=requests.get(url)
        requestsTry-=1
    if(requestsTry==0):
        print("unable to requests.get ",url)
        exit(1)
    else:
        print("requests.get {url} successfully!".format(url=url))
    #以上爬蟲
    #以下分析資料
    html=lxml.etree.HTML(response.content)
    print("len="+str(len(html.xpath('//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div'))))
    for step in range(1,len(html.xpath('//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div'))+1,1):
        path='//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[{step}]/div/a/div[2]/div/div[1]/div/span/text()'.format(step=step)
        print(html.xpath(path)[0])
        path='//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[{step}]/div/a/div[2]/div/div[2]/text()'.format(step=step)
        print(html.xpath(path)[0])

LeetCode()