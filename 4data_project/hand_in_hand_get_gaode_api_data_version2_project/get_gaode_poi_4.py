# 第一步：数据库数据获取，监测30个城市的购物中心
# 第二步：以项目为关键词，对高德地图进行关键词搜索获取相应的poi 每个关键词获取信息不超过500个
# 第三步：数据存储，存储到Excel

# 第一步：获取mysql数据
import pymysql
conn = pymysql.connect(
    host='',
    user='',
    password='',
    port=3306,
    database='',
    charset='utf8'
)

cursor=conn.cursor()

# 查询数据库数据的SQL语句
sql="""
select 
projectid,
projectname,
t2.cityname,
t3.wuyeLx
from project_t1_index t1
left join address_4_city20180124 t2
on t1.ProjectCity = t2.cityid
left join project_t3_protext t3
on t1.ProjectId = t3.for3_ProjectId
where state = 6
and cityname in (
"北京","广州","深圳","上海","成都",
"杭州","武汉","重庆","南京","天津",
"苏州","西安","长沙","沈阳","青岛",
"郑州","大连","宁波","昆明","厦门",
"贵阳","无锡","济南","南昌","东莞",
"福州","合肥","佛山","南通","泉州"
)
and t3.wuyeLx = "购物中心"
"""
cursor.execute(sql)
data=cursor.fetchall()
data1=list(data)
import pandas as pd
mycolumns=["projectid", "projectname", "cityname", "wuyelx"]
data2=pd.DataFrame(data1, columns=mycolumns)

# 数据库数据获取检视
# print(data2)

# 关闭游标和连接
cursor.close()
conn.close()

# 第二步：以项目为关键词，对高德地图进行关键词搜索获取相应的poi
print(data2[["projectname"]])
keywords_list=list(data2.projectname)

# 关键词列表检视
for index in range(3):
    print("序号 %s 值 %s" %(index + 1, keywords_list[index]))
# 项目ID列表
projectid_list=list(data2.projectid)

import xlwt
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
poiTag=["id","name","type","typecode","biz_type","address","location","tel","pname","cityname","adname", "projectid"]
poiSoupTag = ["idSoup","nameSoup","typeSoup","typecodeSoup","biz_typeSoup","addressSoup","locationSoup","telSoup","pnameSoup","citynameSoup","adnameSoup"]

# 正则表达式描述
pattern = re.compile("(?:>)(.*?)(?=<)",re.S)

# 获取信息设置
# offset=25 #每页展示25条（官方限定25条）
# maxPage=10 #设置最多页数（官方限定100页）
maxoffset=25
maxPage=20

# 循环读取每个页面的信息，并且解析出来存储到Excel里面
for i in range(3):
    # 创建Excel表格
    poiExcel = xlwt.Workbook()  # 新建工作簿
    sheet = poiExcel.add_sheet("gaode_poi_result"+str(i))  # 新建gaode_poi_result工作表
    for colIndex in range(len(poiTag)):
        sheet.write(0, colIndex, poiTag[colIndex])
    for pageIndex in range(1, maxPage+1):
        try:
            url = "http://restapi.amap.com/v3/place/text?&keywords=" + urllib.parse.quote(keywords_list[i]) + "&types=" + "&city=" + "&citylimit=true&output=xml&offset=" + str(maxoffset) + "&page=" + str(pageIndex) + "&key=&extensions=base"
            poiSoup = BeautifulSoup(urllib.request.urlopen(url).read(), "xml")
            for tagIndex in range(len(poiTag)-1):
                poiSoupTag[tagIndex] = poiSoup.findAll(poiTag[tagIndex])
            # 结果检视
            # print(poiSoupTag)

            # 把poiSoupTag二维数组解析存放到Excel里面
            for rowIndex in range(len(poiSoupTag[0])):
                for colIndex in range(len(poiSoupTag)):
                    sheet.write(len(poiSoupTag[0]) * (pageIndex - 1) + rowIndex + 1, colIndex,re.findall(pattern, str(poiSoupTag[colIndex][rowIndex])))
            for rowIndex in range(len(poiSoupTag[0])):
                for colIndex in range(len(poiSoupTag), len(poiSoupTag)+1):
                    sheet.write(len(poiSoupTag[0]) * (pageIndex - 1) + rowIndex + 1, colIndex, projectid_list[i])
            # 若果一个页面的行数小于25，说明后面的页面就没有数据啦
            if(len(poiSoupTag[0]) < 25):
                break
        except Exception as e:
            print(e)
    # 第三步：数据保存的Excel
    poiExcel.save("data_output/"+str(projectid_list[i])+".xls")

