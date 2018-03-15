# from bs4 import BeautifulSoup
#
# soup=BeautifulSoup('<p>广州天河城</p>', 'html.parser')
# print(soup)
# print(soup.p.string)
#
# soup1=BeautifulSoup('Hello','lxml')
# print(soup1.p.string)

# BeautifulSoup使用
from bs4 import BeautifulSoup
text = """
<html>  
    <head>
     <title >hello, world</title>
    </head>
    <body>
        <h1>BeautifulSoup</h1>
        <p class="bold">如何使用BeautifulSoup</p>
        <p class="big" id="key1"> 第二个p标签</p>
        <a href="http://foofish.net">python</a>
    </body>
</html>  
"""
soup = BeautifulSoup(text, "html.parser")
print(soup.title)
print(soup.p)
print(soup.p.string)
print(type(soup))
print(type(soup.h1))
print(type(soup.p.string))
print(soup.p.name)
print(soup.h1.name)
print(soup.p['class'])
print(soup.p.string)

# 遍历文档树
print(soup.body)
print(soup.body.p)
print(soup.body.p.string)

# 搜索文档树
# 找到所有标签名为title的节点
print(soup.find_all("title"))
print(soup.find_all("p"))
# 设置标签和属性参数值
print(soup.find_all("p", "big"))
# 或者
print(soup.find_all("p", class_="big"))
print(soup.find_all(href="http://foofish.net"))
# 或者利用正则表达式
import re
print(soup.find_all(href=re.compile("^http")))
# 利用逻辑表达式代表是否有无
print(soup.find_all(id="key1"))
print(soup.find_all(id=True))
# 遍历和搜索相结合
body_tag=soup.body
print(body_tag.find_all("a"))

print(body_tag)
print(body_tag.find("a"))
print(body_tag.find("p"))

# 获取文本信息
p1=body_tag.find('p').get_text()
print(type(p1))
print(p1)
p2=body_tag.find('p').string
print(type(p2))
print(p2)