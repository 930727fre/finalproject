import lxml
import requests
import bs4
import time

print("codeforces.py:")
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
