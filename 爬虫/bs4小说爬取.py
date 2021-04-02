from bs4 import BeautifulSoup
import os
import requests
import time

url = "https://www.shicimingju.com/book/sanguoyanyi.html"
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
html = requests.get( url = url, headers = headers)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text, 'lxml')
li_list = soup.select('.book-mulu > ul> li')
fp = open('./三国演义.txt', 'w', encoding='utf-8')
a = 1
for li in li_list:
    title = li.a.string
    #print(title)
    text_url = "https://www.shicimingju.com/"+li.a['href']
    #print(text_url)
    text_html = requests.get(url = text_url, headers = headers )
    text_html.encoding = 'utf-8'
    soup2 = BeautifulSoup(text_html.text, 'lxml')
    detail_content = soup2.find('div', class_ = 'chapter_content')
    #print(detail_content.text)
    content = detail_content.text
    fp.write(title+':'+'\n'+content+'\n')
    time.sleep(0.5)
    print('第%d章爬取成功'%a)
    a = a+1
print('--over--')
   
    
    




