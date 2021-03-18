import requests
import os
import re

if not os.path.exists("./qiutu"):
    os.mkdir("./qiutu")   
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
url = "https://www.qiushibaike.com/imgrank/page/%d/"
for page_number in range(1,10):
    new_url = format(url%page_number)
    repond = requests.get(url = new_url, headers = headers).text
    # print(repond)
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_text = re.findall(ex, repond, re.S)
    # print(img_text)
    for src in img_text:
        image = 'https:' + src
        image_content = requests.get(url = image, headers = headers).content
        image_name = src.split("/")[-1]
        image_Path = './qiutu/' + image_name
        with open(image_Path, 'wb') as fp:
            fp.write(image_content)
            print('----success-----')
print('---over---')
