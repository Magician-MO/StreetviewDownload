import requests
import time

bs ={'user-agent':'HuoHu/12.0.1'} #浏览器
savePath = "/Users/Meteor/Downloads/"  # 保存路径
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512'
coordtype = "bd09ll"
coordx = 116.403909
coordy = 39.91416
heading = 10
fov = 120
street = "zstreet"
rownum = 2

location = str(coordx) + ',' + str(coordy)
imageName = street + '_' + str(rownum)
fileName = savePath + imageName + '.jpeg'
fileUrl = baseUrl + '&heading=' + \
    str(heading) + '&fov=' + str(fov) + '&coordtype=' + \
    coordtype + '&location=' + location

r = requests.get(fileUrl,headers=bs)
header = dict(r.headers)
print(header)
if(dict(r.headers)['Content-Type'] != "image/jpeg"):
    print("nothing")
#print(fileUrl)
#print(r.headers)

try:
    with open(fileName,'wb') as f:
        f.write(r.content)#返回二进制形式
        f.close()
        print("SUCCESS")
except:
    print('FAILE')
