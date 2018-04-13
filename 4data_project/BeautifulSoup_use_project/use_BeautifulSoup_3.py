#-*- coding:utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup

# 创建一个类，实现封装功能
class BeautifulPicture():
    # 类的初始化操作
    def __init__(self):
        self.headers = {
        'Cookie': 'guid=3cdf-970a-ae6b-8dd0; UM_distinctid=161c57f94943b9-0a575f439620e1-3c604504-13c680-161c57f94956fe; cna=cnqZEk8AxV4CAdxzvVPvzL/k; passport_login=MTY5NDY1Nzg1LGFtYXBfMTM1MzI4MDQ2MDVCOFIxMlphaTEsdTU3bWwxNnYzN281amI3aDF6azV0c2dlMnZwODBwaDIsMTUxOTk3Mjg5MyxNVEUyTnpRNU9EYzBPR0l3TXpaalpUWXlPREU1TldNM1lqZGlNVFJtTm1FPQ%3D%3D; isg=BGVlUV_gU_q627coE3rc7gTjdCFfChhVFncTH2doTRyUfrnxZvK1BN1XDOII_jHs; dev_help=fAJvOLYlCntq6JEmUL14LTZhNTFlMzRkZDJlNzdlZjgzYjdkMjA2ZmNmY2NkMDIyNzFmMGE1ODAzN2Y0OTE2MWU0ZjNiYmM4ZDhhMDI3NGapszj0Xd3zrwzC3yNS6g%2FvcORhnuCXseDAHrvhLZHAj1nPVyn9mPmyrovJbSoetZEd7swBzp0BEJw7ZJcgZiHZSaCDQ9bwOQdPAKuNag2fLvQxlcmBKWvzDMpFZgcP9gY%3D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        }

        self.web_url = 'https://unsplash.com' # 需要访问的网页网址
        self.folder_path = 'E:\BeautifulPicture' # 设置图片要保存的文件目录


    # 获取图片函数
    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签')
        all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='cV68d') # 获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('进入创建的文件夹')
        os.chdir(self.folder_path)

        # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
        for a in all_a:
            img_str = a['style']
            first_pos = img_str.index('"') + 1
            second_pos = img_str.index('"', first_pos)
            img_url = img_str[first_pos:second_pos]
            #获取高度和宽度
            width_pos = img_str.index('&w=')
            height_pos = img_str.index('&q=')
            width_height_str = img_url[width_pos : height_pos]
            print('高度和宽度数据字符串是：' , width_height_str)
            img_url_final = img_url.replace(width_height_str, '') #把高度和宽度的字符串替换成空字符串
            print('截取后图片的url是：', img_url_final)
            # 截取图片名
            name_start_pos = img_url.index('photo')
            name_end_pos = img_url.index('?')
            image_name = img_url[name_start_pos:name_end_pos]
            self.save_img(img_url_final, image_name)

    def save_img(self, url, name):
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功')
        f.close()

    # 向目标url发送get请求函数
    def request(self, url):
        r = requests.get(url, headers = self.headers) # 向目标url地址发送get请求，返回一个response对象
        return r

    # 创建文件夹函数
    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功')
        else:
            print(path,'文件夹已经存在，不再创建')

beauty = BeautifulPicture()  #创建类的实例
beauty.get_pic()  #执行类中的方法



