import requests
import re
import os

if not os.path.exists("./p站"):
    os.mkdir("./p站")

url_1 = "https://rt.huashi6.com/front/works/get_is_like"
headers = {
    'User-Agent': '2Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
respond = requests.post(url = url_1, data = )