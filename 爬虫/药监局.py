import requests
import json

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
id_list = [] #用来存储id值
all_data = [] #用来存储不用页面的数据
for i in range(1,6):
    data = {
        'on': 'true',
        'page': i,
        'pageSize': ' 15',
        'productName': ' ',
        'conditionType': '1',
        'applyname': ' ',
        'applysn': ' ',
    }
    ids = requests.post(url = url, data = data, headers = headers).json()
    #print(ids)

    for dic in ids['list']:
        id_list.append(dic['ID'])
    # print(id_list)
    url_2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data_2 = {
            'id': id
        }
        rel_data = requests.post(url = url_2, data = data_2, headers = headers ).json()
        all_data.append(rel_data)
fp = open('./yaojianju.json', 'w', encoding='utf-8')
json.dump(all_data, fp= fp, ensure_ascii= False, indent= True)
print('------爬取成功-------')








