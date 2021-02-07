from bs4 import BeautifulSoup
import urllib
from urllib import request
html = urllib.request.urlopen('https://sc.chinaz.com/tupian/')
bsobj = BeautifulSoup(html.read())
namelist = bsobj.findAll("img")
for name in namelist:
    print(name)