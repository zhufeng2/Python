import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

data = {
    'cname': '',
    'pid': '',
    'keyword': '武汉',
    'pageIndex': 1,
    'pageSize': '10',
    }
respond = requests.post(url = url,data = data, headers = headers)
text = respond.json()
print(text)
    # 'a'在文件后面写入，不改变文件原来的样子，只在后面进行补充
fp = open('./kfc.json','w',encoding='utf-8')
json.dump(text, fp = fp, ensure_ascii=False)
print('信息爬取并存储完成')
