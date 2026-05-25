# __VIEWSTATE : WZ1UZWzlkaganOCepLIKpQgolzMEqNNYfSrww6LpanH/be+z3JYkuBMZTW/OoUhJZYay6TPrLqUd52CLS/9QqWdUw9SHTwi95Tj0KNo2qHTjUbR8znSLi3uRIBfYuGJnxrM0YoRd7gRsyWx5h3AgZw/OI1Q=
# __VIEWSTATEGENERATOR : C93BE1AE
# from
# email : 15983028818
# pwd : 777974wqh
# code : 97pj
# denglu : 登录

# 我们观察到__VIEWSTATE ， __VIEWSTATEGENERATOR ， code 是变化的

#(1) __VIEWSTATE ， __VIEWSTATEGENERATOR 在页面的源码中，所以我们需要获取源码在解析

import requests

url = 'https://www.gushiwen.cn/user/login.aspx'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}

response = requests.get(url=url,params=headers)
content = response.text
#解析网页源码
import bs4
soup = bs4.BeautifulSoup(content,'lxml')

viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

#获取图片验证码
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://www.gushiwen.cn' + code

#获取图片后下载到本地，然后观察验证码。然后在控制台输入验证码
#用urllib.request.urlretrieve()为导致验证码刷新了两次
#用requests中的方法session() 能使请求变成一个对象
session = requests.session()
response_code = session.get(url=code_url)
content = response_code.content  #图片需要用二进制来写入

with open('code.jpg','wb') as fp:
    fp.write(content)

code_name = input('请输入你的验证码：')

#点击登录
url_post = 'https://www.gushiwen.cn/user/login.aspx'

data_post = {
'__VIEWSTATE' : viewstate,
'__VIEWSTATEGENERATOR' : viewstategenerator,
'from' : '',
'email' : '15983028818',
'pwd' : '777974wqh',
'code' : code_name,
'denglu' : '登录',
}

#代码只获取了登录响应的内容,没有跟随JavaScript 跳转代码跳转
response_post = session.post(url=url_post,data=data_post,headers=headers)
content_post = response_post.text

#直接访问跳转后的页面
response_wode = session.get('https://www.gushiwen.cn/user/wode.aspx', headers=headers)
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(response_wode.text)