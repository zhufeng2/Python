import requests
from lxml import etree
import os
import time

if not os.path.exists("./简历模板爬取"):
    os.mkdir("./简历模板爬取")
i = 0
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}

url = "https://sc.chinaz.com/jianli/biaoge.html"
respond = requests.get(url=url, headers = headers)
respond.encoding = 'utf-8'
#print(respond.text)
respond_data = etree.HTML(respond.text)
#print(respond_data)
list_data = respond_data.xpath('//div[@class="box col3 ws_block"]/a/@href')
file_name = respond_data.xpath('//div[@class="box col3 ws_block"]/p/a/text()')
#print(file_name)
#print(list_data)
# 分析之前找不到可能是因为乱码的缘故,还是就是网页上的和你实际获取的网页源码是不一样的
for list in list_data:
    concret_html = "https:"+list
    concret_respond = requests.get(url = concret_html,headers=headers)
    concret_respond.encoding = 'utf-8'
    concret_respond_data = etree.HTML(concret_respond.text)
    Resume_url = concret_respond_data.xpath('//div[@class="clearfix mt20 downlist"]/ul/li/a/@href')
    if Resume_url == []:
        print("需要付费")
    elif Resume_url != []:
        Resume_url_2 = concret_respond_data.xpath('//div[@class="clearfix mt20 downlist"]/ul/li/a/@href')[0]
        rar_name = str(file_name[i])+'.rar'
        resume_data = requests.get(url = Resume_url_2, headers = headers).content
        resume_path = "./简历模板爬取/"+rar_name
        with open(resume_path, 'wb') as fp:
            fp.write(resume_data) 
            print("--爬取成功--")
            time.sleep(1.0)
    i=i+1 
print("--爬取完成--")