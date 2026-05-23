from lxml import etree
import urllib.request

url = 'https://www.baidu.com/'
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
tree = etree.HTML(content)
text = tree.xpath('//button[@id="chat-submit-button"]/text()')
result = text[0]
print(result)