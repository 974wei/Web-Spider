import urllib
import urllib.request
import json
import jsonpath

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1778921169975_120&jsoncallback=jsonp121&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers ={
    'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'bx-v':'2.5.36',
    'cookie':'cna=DhePIodpYhcCAbaWe4TwKC5T; xlly_s=1; _m_h5_c=ea5e849ec6e7386eaa6acc6f81ea7a06_1778926897470%3B3fa7e3b467576f210eacf986357c8414; tb_city=310100; tb_cityName="yc+6ow=="; isg=BEVFs1Fcg8ydt6cQnkpWR1lqVIF_AvmUfgHldkeqtnyL3mVQD1KrZIKw6AIonhFM',
    'priority':'u=1, i',
    'referer':'https://www.taopiaopiao.com/?spm=a1z21.3046609.city.1.3428112asr8aga&tbpm=3&city=110100',
    'sec-ch-ua':'"Chromium";v="148", "Microsoft Edge";v="148", "Not/A)Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
    'x-requested-with':'XMLHttpRequest',
}

request = urllib.request.Request(url,headers=headers)
respond = urllib.request.urlopen(request)
content = respond.read().decode('utf-8')

# split 切割
content = content.split('(')[1].split(')')[0]#从左右括号处切割后分别依次保留第2，第1个元素

with open('解析-jsonpath解析淘票票.json','w',encoding='utf-8') as f:
    f.write(content)

obj = json.load(open('解析-jsonpath解析淘票票.json','r',encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)
