import xlrd  # 必须事先引入读excel的包xlrd
import urllib.request
import requests

bs ={'user-agent':'HuoHu/12.0.1'} #浏览器
filePath = u"/Users/Meteor/Downloads/coords.xls"  # excel所在路径
savePath = "/Users/Meteor/Downloads/"  # 保存路径

# url
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512&fov=180'
coordtype = "bd09ll"
location = "116.313393,40.04778"
heading = "180"
fov = "120"

try:
    workbook = xlrd.open_workbook(filePath)  # 打开Excel
    sheet = workbook.sheet_by_index(0)  # 第一张sheet表
    nrows = sheet.nrows  # 总行数

    # 遍历对应列的每一行数据
    for rownum in range(nrows):  # 第一行是列名，所以从1开始即第二行读起

        street = sheet.cell(rownum, 0).value
        coordx = sheet.cell(rownum, 1).value
        coordy = sheet.cell(rownum, 2).value
        heading = sheet.cell(rownum, 3).value
        #fov = sheet.cell(rownum,4).value

        location = str(coordx) + ',' + str(coordy)
        imageName = street + '_' + str(rownum)
        fileName = savePath + imageName + '.jpeg'
        fileUrl = baseUrl + '&heading=' + \
            str(heading) + '&fov=' + str(fov) + '&coordtype=' + \
            coordtype + '&location=' + location

        r = requests.get(fileUrl,headers=bs)
        print("image_get - " + imageName, end=' : ')

        if(dict(r.headers)['Content-Type'] != "image/jpeg"):
            print("FALSE === get nothing - " + location)
        else:
            try:
                with open(fileName,'wb') as f:
                    f.write(r.content)#返回二进制形式
                    f.close()
                    print("SUCCESS")
            except:
                print('FAILE')
except Exception as e:
    print('ERROR - ', e)
