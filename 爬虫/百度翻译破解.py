import requests
import json

# 首先我们指定好需要请求的网站
url = 'https://fanyi.baidu.com/sug'
# 在每个爬虫脚本中进行UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# 对网页进行请求
word = input('please input a word:')
data = {'kw': word}
respond = requests.post(url=url, data=data, headers=headers)
# 处理一个json数据,返回一个obj对象
dic_obj = respond.json()
print(dic_obj)
