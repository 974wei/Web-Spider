import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}

data = {
    'kw':'eye'
}

request = requests.post(url=url, data=data, headers=headers)

content = request.text

import json
obj = json.loads(content)
print(obj)
