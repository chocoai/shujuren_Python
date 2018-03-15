# coding =  'utf-8'
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import re
import xlwt
poiTag=["id","name","type","typecode","biz_type","address","location","tel","pname","cityname","adname"]
poiSoupTag = ["idSoup","nameSoup","typeSoup","typecodeSoup","biz_typeSoup","addressSoup","locationSoup","telSoup","pnameSoup","citynameSoup","adnameSoup"]

# 正则表达式描述
pattern = re.compile("(?:>)(.*?)(?=<)",re.S)

poiExcel=xlwt.Workbook() # 新建工作簿
sheet=poiExcel.add_sheet("gaode_poi_result") # 新建gaode_poi_result工作表
for colIndex in range(len(poiTag)):
    sheet.write(0, colIndex, poiTag[colIndex])

url = "http://restapi.amap.com/v3/place/text?&keywords="+ urllib.parse.quote("上海五角场万达广场") + "&types=" + "&city=" + "&citylimit=true&output=xml&offset=" + str(10) + "&page=" + str(1) + "&key=ee01b807a44b0db2b54432c3b3665f9a&extensions=base"
# open_url=urllib.request.urlopen(url)
# print(open_url)

poiSoup = BeautifulSoup(urllib.request.urlopen(url).read(), "xml")
for tagIndex in range(len(poiTag)):
    poiSoupTag[tagIndex] = poiSoup.findAll(poiTag[tagIndex])
# 结果检视
print(poiSoupTag)
# 数据存储
for rowIndex in range(len(poiSoupTag[0])):
    for colIndex in range(len(poiSoupTag)):
        sheet.write(rowIndex + 1, colIndex,re.findall(pattern, str(poiSoupTag[colIndex][rowIndex])))
poiExcel.save("data_output/上海五角场万达广场POI.xls")



# 资料：
# http://blog.csdn.net/u010161379/article/details/50953427
