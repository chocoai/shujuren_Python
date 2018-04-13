# -*- coding:utf-8 -*-
# 从高匿代理ip网站获取可用的代理ip
# 国内高匿代理ip网站:
# http://www.xicidaili.com/nn/

import requests
import random
import codecs
import time
from bs4 import BeautifulSoup

# url = "http://www.xicidaili.com/nn/1"

# web_data = requests.get(url, headers = headers)
# # print(web_data.text)
# soup = BeautifulSoup(web_data.text, 'lxml')
# ips = soup.find_all('tr')
# # print(ips)
# print(len(ips))
# ip_info = ips[1]
# print(ip_info)
# tds = ip_info.find_all('td')
# print(tds[0])
# print(tds[1])
# print(tds[2])
# print(tds[1].text)
# print(tds[2].text)

# 获取ip列表
def get_ip_list(url, headers):
    web_data = requests.get(url, headers = headers)
    print(web_data)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

# ip随机获取
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http':proxy_ip}
    return proxies

def get_community_message(community_url,proxy,header):
    for k in range(1, 6):
        try:
            res = requests.get(community_url, headers=header, proxies=proxy, timeout=5)
            res.encoding = 'gb18030'
            soup = BeautifulSoup(res.text, 'html.parser')
            break
        except:
            if k < 5:
                print(k)
                time.sleep(0.5)
                continue
            else:
                print('ip_error')
                break
                # print 'step 1 over'
    # community_name = soup.find(class_='tt').get_text()

# 验证ip是否可用
def ip_check(ip):
    proxy_ip = 'http://' + ip
    community_url = 'http://16jiequdhjxhc.fang.com/xiangqing/'
    proxies = {'http': proxy_ip}
    headers = {
        'Cookie': 'guid=3cdf-970a-ae6b-8dd0; UM_distinctid=161c57f94943b9-0a575f439620e1-3c604504-13c680-161c57f94956fe; cna=cnqZEk8AxV4CAdxzvVPvzL/k; passport_login=MTY5NDY1Nzg1LGFtYXBfMTM1MzI4MDQ2MDVCOFIxMlphaTEsdTU3bWwxNnYzN281amI3aDF6azV0c2dlMnZwODBwaDIsMTUxOTk3Mjg5MyxNVEUyTnpRNU9EYzBPR0l3TXpaalpUWXlPREU1TldNM1lqZGlNVFJtTm1FPQ%3D%3D; isg=BGVlUV_gU_q627coE3rc7gTjdCFfChhVFncTH2doTRyUfrnxZvK1BN1XDOII_jHs; dev_help=fAJvOLYlCntq6JEmUL14LTZhNTFlMzRkZDJlNzdlZjgzYjdkMjA2ZmNmY2NkMDIyNzFmMGE1ODAzN2Y0OTE2MWU0ZjNiYmM4ZDhhMDI3NGapszj0Xd3zrwzC3yNS6g%2FvcORhnuCXseDAHrvhLZHAj1nPVyn9mPmyrovJbSoetZEd7swBzp0BEJw7ZJcgZiHZSaCDQ9bwOQdPAKuNag2fLvQxlcmBKWvzDMpFZgcP9gY%3D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    try:
        get_community_message(community_url, proxies, headers)
        return True
    except:
        return False

if __name__ == '__main__':
    ip_list = []
    ip_txt = "scraping_ip.csv"
    url_s = 'http://www.xicidaili.com/nn/'
    headers = {
        'Cookie': 'guid=3cdf-970a-ae6b-8dd0; UM_distinctid=161c57f94943b9-0a575f439620e1-3c604504-13c680-161c57f94956fe; cna=cnqZEk8AxV4CAdxzvVPvzL/k; passport_login=MTY5NDY1Nzg1LGFtYXBfMTM1MzI4MDQ2MDVCOFIxMlphaTEsdTU3bWwxNnYzN281amI3aDF6azV0c2dlMnZwODBwaDIsMTUxOTk3Mjg5MyxNVEUyTnpRNU9EYzBPR0l3TXpaalpUWXlPREU1TldNM1lqZGlNVFJtTm1FPQ%3D%3D; isg=BGVlUV_gU_q627coE3rc7gTjdCFfChhVFncTH2doTRyUfrnxZvK1BN1XDOII_jHs; dev_help=fAJvOLYlCntq6JEmUL14LTZhNTFlMzRkZDJlNzdlZjgzYjdkMjA2ZmNmY2NkMDIyNzFmMGE1ODAzN2Y0OTE2MWU0ZjNiYmM4ZDhhMDI3NGapszj0Xd3zrwzC3yNS6g%2FvcORhnuCXseDAHrvhLZHAj1nPVyn9mPmyrovJbSoetZEd7swBzp0BEJw7ZJcgZiHZSaCDQ9bwOQdPAKuNag2fLvQxlcmBKWvzDMpFZgcP9gY%3D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    for j in range(1, 2):
        url_m = url_s + str(j)
        ip_interim= get_ip_list(url_m, headers=headers)
        for k in ip_interim:
            if ip_check(k):
                #ip_list.append(k)
                # codecs的open函数
                # 参数mode = 'a' 表示文件末尾添加内容
                # 刚开始若是没有文件，先创建文件
                csvfile = codecs.open(ip_txt, "a", encoding='gbk', errors='ignore')
                csvfile.write('%s \n' % (k))
                csvfile.close()