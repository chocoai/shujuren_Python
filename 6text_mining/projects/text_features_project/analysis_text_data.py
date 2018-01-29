import re
import os
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def geturl(url):
    try :
        html = urlopen(url)
    except HTTPError as e :
        return None
    try :
        bsObj = BeautifulSoup(html, 'lxml')
    except AttributeError as e :
        return None
    return bsObj
def getArticle(url, f) :
    articlePage = geturl(url)
    article = articlePage.findAll('p')
    for paragraph in article :
        print (paragraph.get_text(), file = f)
start = "http://www.kanunu8.com/book/4433/"
page = geturl(start)
tr = page.findAll('tr', {'bgcolor' : '#ffffff'})
links = (re.findall(r'<td><a href="(.*?)">(.*?)</a></td>', str(tr)))
if not os.path.isdir('article') :
    os.mkdir('article')
for link in links :
    with open('./article/' + link[1] + '.txt', 'wt+') as f :
        f.write(link[1])
        getArticle(start + link[0], f)
    print ('---< ' , link[1], ' > get ---')