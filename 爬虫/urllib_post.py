import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0'
}

data = {
    'kw' : 'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

requset = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(requset)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)