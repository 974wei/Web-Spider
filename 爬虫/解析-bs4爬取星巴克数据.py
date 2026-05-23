import urllib
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.hk/zh_HK/catalog/category/view/id/70/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content= response.read().decode('utf-8')

soup = BeautifulSoup(content,'lxml')
name_list = soup.select('a[class="product-item-link"]')#  我这个查询获取的是 焦糖咖啡 </a>, <a class="product-item-link" href="https://www.starbucks.com.hk/zh_HK/pure-matcha-latte.html">

product_names = [a.get_text(strip=True) for a in name_list]# 可以去掉后面的标签，strip=True 去除文本首尾的空白字符（换行、空格等）

for product in product_names:
    print(product)
