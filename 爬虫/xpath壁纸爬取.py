from lxml import etree
import requests
import os
import time

if not os.path.exists('./壁纸'):
    os.mkdir('./壁纸')
i = 0
url = "http://www.jj20.com/bz/nxxz/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
initial_page = requests.get(url=url,headers=headers)
initial_page.encoding = 'gbk'
initial_respond = etree.HTML(initial_page.text)
url_lists = initial_respond.xpath('//div[@class="g-box-1200"]/ul/li/a[1]/@href')
for url_list in url_lists:
    img_url = "http://www.jj20.com/"+url_list
    img_url_page = requests.get(url = img_url,headers = headers)
    img_url_page.encoding='gbk'
    img_url_respond = etree.HTML(img_url_page.text)
    img_list=img_url_respond.xpath('//div[@class="wra"]//img/@src')[0]
    file = requests.get(url = img_list, headers=headers).content
    #print(img_list)
    file_name = "./壁纸/"+str(i)+".jpg"
    with open(file_name,'wb') as fp:
        fp.write(file)
    print('--爬取成功--')
    i=i+1
    time.sleep(1.5)
print("爬取完成")

    


