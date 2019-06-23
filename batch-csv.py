# coding: utf-8
import csv
import urllib.request
import requests
import json

bs ={'user-agent':'HuoHu/12.0.1'} #浏览器
filePath = u"./data/input.csv"  # 文件路径
savePath = "./image/"  # 保存路径

# url
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512&fov=180'
coordtype = "wgs84ll"
location = "116.313393,40.04778"
headingA = "180"
headingB = "0"
fov = "120"

def image_get(street, coordx, coordy, order, heading):
    location = str(coordx) + ',' + str(coordy)
    imageName = street + '_' + str(order) + '_' + str(heading)
    fileName = savePath + imageName + '.jpg'
    fileUrl = baseUrl + '&heading=' + \
        str(heading) + '&fov=' + str(fov) + '&coordtype=' + \
        coordtype + '&location=' + location

    r = requests.get(fileUrl,headers=bs)
    print("image_get - " + imageName, end=' : ')

    if(dict(r.headers)['Content-Type'] != "image/jpeg"):
        print("FAILE", end=' === ')
        print(r.json()['message'])
    else:
        try:
            with open(fileName,'wb') as f:
                f.write(r.content)#返回二进制形式
                f.close()
                print("SUCCESS")
        except Exception as e:
            print('FAILE === ',e)

file = open(filePath)
#reader = csv.reader(file)
# 字典式读取方式
# OBJECTID,PNT_ORDER,ROAD_NAME,POINT_X,POINT_Y
reader = csv.DictReader(file)
for row in reader:
    order = row['ID']
    street = row['STREET']
    headingA = row['DIRECTION_A']
    headingB = row['DIRECTION_B'] 
    coordx = row['POINT_X']
    coordy = row['POINT_Y']

    image_get(street, coordx, coordy, order, headingA)
    image_get(street, coordx, coordy, order, headingB)
