# 一 爬虫请求库
# 1 requests库的安装 pip install requests
# 2 selenium库的安装 pip install selenium
# 3 aiohttp库的安装 pip install aiohttp
# 4 cchardet aiodns库的安装 pip install cchardet aiodns

# 二 爬虫解析库
# pip install lxml库
# pip install beautifulsoup4库
# pip install pyquery库
# pip3 install tesserocr pillow 验证码识别库





import requests
# from selenium import webdriver
# browser=webdriver.Chrome()

# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('https://www.baidu.com')
# print(browser.current_url)

from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)






