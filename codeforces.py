import lxml, requests, bs4, time, json, datetime

def cf():
    url="https://codeforces.com/api/contest.list"
    response=requests.get(url)
    requests_try=3
    while requests_try and response.status_code!=200:
        requests_try -= 1
        time.sleep(2)
    if response.status_code!=200:
        print("unable to GET from ", url)
        print("status code :", response.status_code)
        print("reaon :", response.reason)
        quit()
    r=response.json() #shorten for response
    contests=[]
    for contest in r['result']:
        if contest['relativeTimeSeconds']<0 and -5260000<contest['relativeTimeSeconds']: # date range: 2 months
            contests.append({
                "name": contest['name'],
                "startTime": contest['startTimeSeconds']
            })
    file=open("codeforces.json",'w+')
    json.dump(contests,file)
    file.close()

cf()