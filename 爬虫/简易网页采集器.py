import requests
# 注意我们需要对爬虫程序进行UA伪装，封装到一个字典中
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
# 首先我们可以得到需要定义需要请求的网站,注意类型是字符串类型的
url = 'https://www.sogou.com/web'
# 现在对该程序进行get请求,在此之前我们需要对其进行定义搜索关键字
# 由一个动态字典的形式给出
kw = input('please input a keyword:')
param = {'query': kw}
response = requests.get(url=url, params=param, headers=headers)
# 请求到网站中从网站中进行获取内容，这里获取的是文本
page_text = response.text
filename = kw + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(filename, '保存成功')
