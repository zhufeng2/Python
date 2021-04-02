import requests
url = "http://www.jj20.com/bz/nxxz/shxz/323596.html"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
real_html = requests.get(url=url,headers=headers)
real_html.encoding = 'gbk'
print(real_html.text)




