from bs4 import BeautifulSoup
import requests
import os,sys
from PIL import Image
from io import BytesIO

width = 3
depth = 2
urllist = []
orgin_url = 'http://www.nenmj.com/1/'

base = 'D:/IMAGES/'
m = 1
for m in range(10):
    file_name = base+str(m)
    os.mkdir(file_name)
    m = m+1

for j in range(width):
    start_url = orgin_url + str(j + 7410) + '.html'
    urllist = []
    for i in range(depth):
        url = start_url + '?page=' + str(i + 1)
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text, 'lxml')
        for imglist in soup.select('body > div > div > div.col-md-9 > div > img'):
            urllist.append(imglist.get('src'))
    x = 0
    for imgurl in urllist:
        iurl = requests.get(imgurl)
        image = Image.open(BytesIO(iurl.content))
        path = 'D:/IMAGES/%s/' %j + '%s.jpg'%x
        image.save(path)
        x +=1