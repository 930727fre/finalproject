import lxml, requests, bs4, time, json, datetime

def zerojudge():
    url="https://zerojudge.tw/Contests"
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
    html=lxml.etree.HTML(response.content)
    contests=[]
    for step in range(1,len(html.xpath("//div[@class='container-fluid']")),1):
        path="//div[@class='container-fluid'][{step}]//div[@class='col-md-8']/h1/text()".format(step=step)
        name=html.xpath(path)[0]
        path="//div[@class='container-fluid'][{step}]//div[@class='col-md-8']/pre/text()".format(step=step)
        if(len(html.xpath(path))==0):
            comment="NULL"
        else:
            comment=html.xpath(path)[0]
        path="/html/body/div[3]/div/div[{step}]/div/div/div[2]/div/div[1]/text()[2]".format(step=step)
        startTime=html.xpath(path)[0].split('：')[1].split('.')[0]
        startTime = time.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        endTime = str(int(time.mktime(startTime))+7200)+'000'
        startTime = str(int(time.mktime(startTime)))+'000'
        
        contests.append({
            "title": name,
            "start": startTime,
            "end": endTime,
            "comment": comment
        })   
    file=open("./jsons/zerojudge.json",'w')
    json.dump(contests,file)
    file.close()             
