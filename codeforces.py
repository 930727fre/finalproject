import lxml, requests, bs4, time, json, datetime

def cf():
    url="https://codeforces.com/api/contest.list"
    response=requests.get(url)
    requests_try=3
    while requests_try and not response.ok:
        requests_try -= 1
        time.sleep(2)
        response=requests.get(url)
    if not response.ok:
        print("unable to requests.get ",url)
        exit(0)
    else:
        print("requests.get %s successfully!"%url)
    r=response.json() #shorten for response
    contests=[]
    for contest in r['result']:
        if (contest['phase']=="CODING" or contest['phase']=="BEFORE") and -5260000<contest['relativeTimeSeconds']: # date range: 2 months
            contests.append({
                "name": contest['name'],
                "startTime": contest['startTimeSeconds'],
                "comment": "NULL"
            })
    file=open("./jsons/codeforces.json",'w')
    json.dump(contests,file)
    file.close()
