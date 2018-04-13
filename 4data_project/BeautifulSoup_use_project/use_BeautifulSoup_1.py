from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
print(tag)
print(type(tag))

print(tag.name)
# tag.name = "blockquote"
# print(tag)
# print(tag.b)
print(tag['class'])
print(tag.attrs)

tag['class'] = 'verybold'
tag['id'] = 1
print(tag)

# 删除属性
del tag['id']
print(tag)

