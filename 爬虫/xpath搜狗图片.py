from lxml import etree
import requests
import os


url = "https://pic.sogou.com/pics/recommend?category=%E5%A3%81%E7%BA%B8&from=home#%E5%8A%A8%E7%89%A9"
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
html = requests.get( url = url, headers = headers)
print(html.text)
respond = etree.HTML(html.text)
a_list = respond.xpath('//div[@class="main"]//div[@class = "pic"]')
print(a_list)
for a in a_list:
    r = a.xpath('//dic[@class = "pic-box"]/a/@href/text()')
    print(r)
