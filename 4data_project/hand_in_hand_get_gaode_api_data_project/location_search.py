# 基于高德地图的周边搜索
# 服务于project的aoi
# type类型：通行设施;建筑物门;建筑物正门
# typecode:991001

#coding:utf-8
# 任务：
# 任务：
# 1）：获取北京-上海-广州-深圳-成都-杭州六个城市购物中心的区域搜索POI
# 2）：获取武汉-重庆-南京-天津-苏州-西安-长沙-沈阳八个城市购物中心的区域搜索POI
# 3) ：获取余下16个城市的购物中心区域搜索POI

# 基于高德地图API的多边形搜索获取数据

# 第一步：从数据库读取目标项目的数据

"""
赢商大数据监测的30个城市名单：
"北京","广州","深圳","上海","成都",
"杭州","武汉","重庆","南京","天津",
"苏州","西安","长沙","沈阳","青岛",
"郑州","大连","宁波","昆明","厦门",
"贵阳","无锡","济南","南昌","东莞",
"福州","合肥","佛山","南通","泉州"
"""

import pymysql
import pandas as pd
import requests
import json

# 第一步：数据库连接
conn1 = pymysql.connect(
    host = '',
    user = '',
    password = '',
    port = 3306,
    database = '',
    charset='utf8'
)
cursor=conn1.cursor()
sql="""

"""

cursor.execute(sql)
data=cursor.fetchall()
data1=list(data)

mycolumns=["projectid", "projectname", "cityname", "wuyelx", "GD_Lng", "GD_Lat"]
data2=pd.DataFrame(data1, columns=mycolumns)

# 数据检视
print(data2.head())
print(data2.shape[0])
cursor.close()
conn1.close()


# 第二步：数据获取部分
# 设置API参数
offset=50
radius=150
URL1='http://restapi.amap.com/v3/place/around?&key=&radius='+str(radius)+'&offset='+ str(offset) + '&types=991001&output=json&page='
URL2="&location="


# HTML头部参数设置
headers = {
    'Cookie':'guid=3cdf-970a-ae6b-8dd0; UM_distinctid=161c57f94943b9-0a575f439620e1-3c604504-13c680-161c57f94956fe; cna=cnqZEk8AxV4CAdxzvVPvzL/k; passport_login=MTY5NDY1Nzg1LGFtYXBfMTM1MzI4MDQ2MDVCOFIxMlphaTEsdTU3bWwxNnYzN281amI3aDF6azV0c2dlMnZwODBwaDIsMTUxOTk3Mjg5MyxNVEUyTnpRNU9EYzBPR0l3TXpaalpUWXlPREU1TldNM1lqZGlNVFJtTm1FPQ%3D%3D; isg=BGVlUV_gU_q627coE3rc7gTjdCFfChhVFncTH2doTRyUfrnxZvK1BN1XDOII_jHs; dev_help=fAJvOLYlCntq6JEmUL14LTZhNTFlMzRkZDJlNzdlZjgzYjdkMjA2ZmNmY2NkMDIyNzFmMGE1ODAzN2Y0OTE2MWU0ZjNiYmM4ZDhhMDI3NGapszj0Xd3zrwzC3yNS6g%2FvcORhnuCXseDAHrvhLZHAj1nPVyn9mPmyrovJbSoetZEd7swBzp0BEJw7ZJcgZiHZSaCDQ9bwOQdPAKuNag2fLvQxlcmBKWvzDMpFZgcP9gY%3D',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
}

def get_url(url):
    global content,cinema_content,total_num
    try:
        resp = requests.get(url,headers=headers,timeout=3)
        content = json.loads(resp.content)
        total_num = content['count']
        cinema_content = content['pois']
        return content,cinema_content,total_num
    except:
        print('error1')

def get_content(projectid):
    global list1
    num = len(cinema_content)
    list1 = []
    for i in range(num):
        id = cinema_content[i]['id']
        name = cinema_content[i]['name']
        type = cinema_content[i]['type']
        typecode=cinema_content[i]['typecode']
        address = cinema_content[i]['address']
        location = cinema_content[i]['location']
        pname = cinema_content[i]['pname']
        cityname = cinema_content[i]['cityname']
        adname = cinema_content[i]['adname']
        projectid = str(projectid)
        list2 = [id, name, type, typecode, address, location, pname, cityname, adname, projectid]
        list1.append(list2)
    return list1


# 第四步：把获取到的数据存放到mysql数据库里面
# conn2 = pymysql.connect(
#     host='192.168.1.21',
#     user='root',
#     password='123456',
#     database='wlq_data',
#     charset='utf8'
# )
#
# def save_info():
#     try:
#         with conn2.cursor() as cursor2:
#             for str in list1:
#                 sql="insert into xiangmu_location_poi1 (id, name, type, typecode, address, location, pname, cityname, adname, projectid) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" %(str[0],str[1],str[2],str[3],str[4],str[5],str[6],str[7],str[8],str[9])
#                 cursor2.execute(sql)
#         conn2.commit()
#     except:
#         print('error2')

# 把数据保存为csv文件格式
def save_csv(projectid,  page):
    df=pd.DataFrame(list1, columns=["id", "name", "type", "typecode", "address", "location", "pname", "cityname", "adname", "projectid"])
    df.to_csv("data_output_location/"+str(projectid)+"_" +  str(page)+".txt", index=False, sep="\t")


def main():
    project_number=data2.shape[0]
    print("总项目数："+str(project_number))
    for index in range(project_number):
        location = str(round(data2.GD_Lng[index], 6)) + "," + str(round(data2.GD_Lat[index], 6))
        url=URL1+'1'+URL2+location
        get_url(url)
        # page=int(total_num)//offset + 2
        page=2
        for i in range(1, page):
            url = URL1 + str(i) + URL2 + location
            get_url(url)
            get_content(data2.projectid[index])
            save_csv(data2.projectid[index], i)

        project_number=project_number-1
        print("还剩" + str(project_number) + "个项目")

if __name__=='__main__':
    main()
