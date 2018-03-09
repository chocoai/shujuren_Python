# from urllib.request import urlopen
# html=urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html=urlopen("http://pythonscraping.com/pages/page1.html")
# bsObj=BeautifulSoup(html.read())
# print(bsObj.h1)

# 更加稳健的代码
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from bs4 import BeautifulSoup
#
# def getTitle(url):
#     try:
#         html=urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj=BeautifulSoup(html.read(), "lxml")
#         title=bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
#
# title=getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title==None:
#     print("Title could not be found")
# else:
#     print(title)

# 处理更加复杂的html文档
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html, "lxml")
nameList=bsObj.findAll("span", {"class":"green"})
print(nameList)
for name in nameList:
    print(name.get_text())

