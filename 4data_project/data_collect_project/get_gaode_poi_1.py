import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
poiTag=["id","name","type","typecode","biz_type","address","location","tel","pname","cityname","adname"]
poiSoupTag = ["idSoup","nameSoup","typeSoup","typecodeSoup","biz_typeSoup","addressSoup","locationSoup","telSoup","pnameSoup","citynameSoup","adnameSoup"]

# 正则表达式描述
pattern = re.compile("(?:>)(.*?)(?=<)",re.S)

# 创建Excel表格
poiExcel=xlwt.Workbook() # 新建工作簿
sheet=poiExcel.add_sheet("gaode_poi_result") # 新建gaode_poi_result工作表
for colIndex in range(len(poiTag)):
    sheet.write(0, colIndex, poiTag[colIndex])

# 获取信息设置
# offset=25 #每页展示25条（官方限定25条）
# maxPage=10 #设置最多页数（官方限定100页）
offset=25
maxPage=2
city="440106" # 广州天河区
types="120000" # 商务住宅
# 循环读取每个页面的信息，并且解析出来存储到Excel里面
for pageIndex in range(1, maxPage+1):
    try:
        # 目标api链接
        url="http://restapi.amap.com/v3/place/text?&keywords=&types="+types+"&city="+city+"&citylimit=true&output=xml&offset="+str(offset)+"&page="+str(pageIndex)+"&key=ee01b807a44b0db2b54432c3b3665f9a&extensions=base"
        poiSoup=BeautifulSoup(urllib.request.urlopen(url).read(),"xml")
        for tagIndex in range(len(poiTag)):
            poiSoupTag[tagIndex]=poiSoup.findAll(poiTag[tagIndex])
        # 结果检视
        # print(poiSoupTag)

        # 把poiSoupTag二维数组解析存放到Excel里面
        for rowIndex in range(len(poiSoupTag[0])):
            for colIndex in range(len(poiSoupTag)):
                sheet.write(len(poiSoupTag[0]) * (pageIndex - 1) + rowIndex + 1, colIndex,re.findall(pattern, str(poiSoupTag[colIndex][rowIndex])))
        # 结果检视
        # print(sheet)
    except Exception as e:
        print(e)

# 数据保存到Excel
poiExcel.save("data_output/"+types+"&"+city+".xls")



