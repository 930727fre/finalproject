import requests

url = "https://leetcode.com/contest/"
htmlfile = requests.get(url)
print(type(htmlfile))
