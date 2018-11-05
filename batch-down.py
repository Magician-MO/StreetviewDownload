import xlrd  # 必须事先引入读excel的包xlrd
import urllib
import urllib2
import re

filePath = u"/Users/Meteor/Downloads/coords.xls"  # excel所在路径
savePath = "/Users/Meteor/Downloads"  # 保存路径

# url
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512&fov=180'
coordtype = "bd09ll"
location = "116.313393,40.04778"
heading = "180"

try:
    workbook = xlrd.open_workbook(filePath)  # 打开Excel
    sheet = workbook.sheet_by_index(0)  # 第一张sheet表
    nrows = sheet.nrows  # 总行数

    # 遍历对应列的每一行数据
    for rownum in range(1, 2):  # 第一行是列名，所以从1开始即第二行读起

        street = sheet.cell(rownum, 1).value
        coordx = sheet.cell(rownum, 2).value
        coordy = sheet.cell(rownum, 3).value
        heading = sheet.cell(rownum, 4).value

        location = coordx + ',' + coordy
        name = street + '_' + str(rownum)
        fileName = savePath + name + '.jpeg'
        fileUrl = baseUrl + '&' + coordtype + '&' + location + '&' + heading

        urllib.urlretrieve(fileUrl, fileName)
        print ("Succeed: " + name)
except:
    print (str(e))
