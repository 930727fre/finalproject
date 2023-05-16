import urllib.request as req
#from bs4 import BeautifulSoup
#import bs4

#import lxml, requests, bs4, time, json, datetime

#crawler
url = "https://leetcode.com/contest/"

request = req.Request(url, headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#bs4