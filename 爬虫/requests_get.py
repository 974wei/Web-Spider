import requests

url = 'https://cn.bing.com/search?'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'
}

data = {
    'q':'北京'
}

response = requests.get(url=url,params=data,headers=headers)
content = response.text
print(content)