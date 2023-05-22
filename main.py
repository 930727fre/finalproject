import lxml, os, requests, bs4
import codeforces, zerojudge, json, leetcode

statusJson=[]
print("main.py:")
print("codeforces.py:")
statusJson.append({"codeforces": codeforces.cf()}) 
print("zerojudge.py")
statusJson.append({"zerojudge": zerojudge.zj()}) 
print("leetcode.py")
statusJson.append({"leetcode": leetcode.lc()}) 

file=open("./jsons/status.json",'w')
json.dump(statusJson, file)
file.close()