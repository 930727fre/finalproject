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
    data = response.text
    soup = bs(data, 'html.parser')
    a_tags = soup.find_all('a', class_ = 'h-full w-full')
    #"div", {"class": "swiper-slide w-auto mr-0"}
    #<div class="swiper-slide w-auto mr-0 swiper-slide-active" style="margin-right: 16px;"><div class="bg-layer-1 dark:bg-dark-layer-1 group flex flex-col h-[233px] w-[313px] lc-md:h-[280px] lc-md:w-[385px] hover:shadow-level4 transition-shadow dark:hover:shadow-dark-level4 rounded-[13px]" style="box-shadow: rgba(0, 0, 0, 0.04) 0px 2px 6px, rgba(0, 0, 0, 0.02) 0px 4px 8px, rgba(0, 0, 0, 0.02) 0px 6px 12px;"><a href="/contest/weekly-contest-345" class="h-full w-full"><div class="relative rounded-[13px] h-[167px] min-h-[167px] lc-md:h-[194px] lc-md:min-h-[194px]"><div class="h-full w-full"><img src="/_next/static/images/weekly-default-553ede7bcc8e1b4a44c28a9e4a32068c.png" alt="Weekly Contest 345" class="h-full w-full object-cover rounded-t-[13px]"></div><div class="absolute top-0 right-0"><div class="m-4 flex cursor-pointer rounded-2xl bg-black bg-opacity-20 p-1 transition-colors hover:bg-opacity-40"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="text-[24px] text-white"><path fill-rule="evenodd" d="M19 11.063V7h-2v1a1 1 0 11-2 0V7H9v1a1 1 0 01-2 0V7H5v4.063h14zm0 2H5V19h14v-5.938zM9 5h6V4a1 1 0 112 0v1h2a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2V4a1 1 0 012 0v1z" clip-rule="evenodd"></path></svg></div></div><div class="absolute bottom-0 flex w-full items-end text-white _3LEKb h-8 py-2 px-4 lc-md:h-16 lc-md:py-3"><div class="flex items-center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="mr-2 text-base lc-md:text-lg"><path fill-rule="evenodd" d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 100-16 8 8 0 000 16zm1-13.4v4.782l3.047 1.524a1 1 0 11-.894 1.788l-3.6-1.8A1 1 0 0111 12V6.6a1 1 0 112 0z" clip-rule="evenodd"></path></svg>Starts in 11h 24m 54s</div></div></div><div class="flex items-center min-h-[80px] px-4 lc-md:min-h-[84px]"><div class="h-[54px]"><div class="font-medium text-[17px] leading-[22px] lc-md:text-xl text-label-1 dark:text-dark-label-1"><div class="truncate"><span class="transition-colors group-hover:text-blue-s dark:group-hover:text-dark-blue-s">Weekly Contest 345</span></div></div><div class="flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2">Sunday 10:30 AM GMT+8</div></div></div></a></div></div>
    #<div class="swiper-slide w-auto mr-0 swiper-slide-next" style="margin-right: 16px;"><div class="bg-layer-1 dark:bg-dark-layer-1 group flex flex-col h-[233px] w-[313px] lc-md:h-[280px] lc-md:w-[385px] hover:shadow-level4 transition-shadow dark:hover:shadow-dark-level4 rounded-[13px]" style="box-shadow: rgba(0, 0, 0, 0.04) 0px 2px 6px, rgba(0, 0, 0, 0.02) 0px 4px 8px, rgba(0, 0, 0, 0.02) 0px 6px 12px;"><a href="/contest/biweekly-contest-104" class="h-full w-full"><div class="relative rounded-[13px] h-[167px] min-h-[167px] lc-md:h-[194px] lc-md:min-h-[194px]"><div class="h-full w-full"><img src="/_next/static/images/biweekly-default-f5a8fc3be85b6c9175207fd8fd855d47.png" alt="Biweekly Contest 104" class="h-full w-full object-cover rounded-t-[13px]"></div><div class="absolute top-0 right-0"><div class="m-4 flex cursor-pointer rounded-2xl bg-black bg-opacity-20 p-1 transition-colors hover:bg-opacity-40"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="text-[24px] text-white"><path fill-rule="evenodd" d="M19 11.063V7h-2v1a1 1 0 11-2 0V7H9v1a1 1 0 01-2 0V7H5v4.063h14zm0 2H5V19h14v-5.938zM9 5h6V4a1 1 0 112 0v1h2a2 2 0 012 2v12a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2V4a1 1 0 012 0v1z" clip-rule="evenodd"></path></svg></div></div><div class="absolute bottom-0 flex w-full items-end text-white _3LEKb h-8 py-2 px-4 lc-md:h-16 lc-md:py-3"><div class="flex items-center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" fill="currentColor" class="mr-2 text-base lc-md:text-lg"><path fill-rule="evenodd" d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 100-16 8 8 0 000 16zm1-13.4v4.782l3.047 1.524a1 1 0 11-.894 1.788l-3.6-1.8A1 1 0 0111 12V6.6a1 1 0 112 0z" clip-rule="evenodd"></path></svg>Ends in 0h 53m 44s</div></div></div><div class="flex items-center min-h-[80px] px-4 lc-md:min-h-[84px]"><div class="h-[54px]"><div class="font-medium text-[17px] leading-[22px] lc-md:text-xl text-label-1 dark:text-dark-label-1"><div class="truncate"><span class="transition-colors group-hover:text-blue-s dark:group-hover:text-dark-blue-s">Biweekly Contest 104</span></div></div><div class="flex items-center text-[14px] leading-[22px] text-label-2 dark:text-dark-label-2">Saturday 10:30 PM GMT+8</div></div></div></a></div></div>
    for tag in a_tags:
        print(tag.text)
    contests = []
    
    file=open("./leetcode.json",'w')
LeetCode()


