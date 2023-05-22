import lxml, requests, time, json, datetime, re
from bs4 import BeautifulSoup as bs
from dateutil import parser, rrule
from datetime import datetime, timedelta

def lc():
    url="https://leetcode.com/contest/"
    response=requests.get(url)
    requestsTry=5
    while(not response.ok and requestsTry>0):
        time.sleep(1)
        response=requests.get(url)
        requestsTry-=1
    if(requestsTry==0):
        print("unable to requests.get ",url)
        return 0
    else:
        print("requests.get {url} successfully!".format(url=url))
    contests = []
    #以上爬蟲
    #以下分析資料
    html=lxml.etree.HTML(response.content)
    #print("len="+str(len(html.xpath('//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div'))))
    for step in range(1,len(html.xpath('//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div'))+1,1):
        path='//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[{step}]/div/a/div[2]/div/div[1]/div/span/text()'.format(step=step)
        #print(html.xpath(path)[0])
        name = html.xpath(path)[0]
        path='//*[@id="__next"]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[{step}]/div/a/div[2]/div/div[2]/text()'.format(step=step)
        #print(html.xpath(path)[0])
        startTimeRelative = html.xpath(path)[0]

        # 現在的時間
        now = datetime.now()
        days_until_saturday = (rrule.rrule(rrule.WEEKLY, byweekday=5).after(now) - now).days
        saturday_date = now + timedelta(days=days_until_saturday)
        # 解析時間
        event_time = parser.parse(startTimeRelative.split(" ", 1)[1])
        # 組合日期與時間
        startTime = saturday_date.replace(hour=event_time.hour, minute=event_time.minute, second=event_time.second)
        startTime = int(time.mktime(startTime.timetuple())) * 1000
        
        contests.append({
            "name":name,
            "startTime":str(startTime),  # 轉換為字串
        })

    file=open("./leetcode.json",'w')
    json.dump(contests, file)
    file.close()
    return 1
