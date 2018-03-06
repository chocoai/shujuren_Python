# 根据中心点的经纬度计算机正方形四个点的经纬度
import math
r=6371 # 地球半径千米

def findNeighPosition(longitude,latitude, dis):
    dlng=2*math.asin(math.sin(dis/(2*r))) / math.cos(latitude*math.pi/180)
    dlng=dlng*180/math.pi # 角度转换为弧度
    dlat=dis/r
    dlat=dlat*180/math.pi
    minlat=round(latitude-dlat,6)
    maxlat=round(latitude+dlat,6)
    minlng=round(longitude-dlng,6)
    maxlng=round(longitude+dlng,6)
    left_top=[minlng, maxlat]
    right_bottom=[maxlng, minlat]
    return [left_top, right_bottom]

# 以上海五角万达广场为例
lng = round(121.51360321044922, 6)
print(lng)
lat = round(31.301286697387695, 6)
print(lat)

# 计算以经纬度为中心的5千米范围的正方形
print(findNeighPosition(lng, lat, 5))
