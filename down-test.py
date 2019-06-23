import urllib.request

savePath = "/Users/Meteor/Downloads/"  # 保存路径

# url
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512'
coordtype = "bd09ll"
coordx = 116.403909
coordy = 39.91416
heading = 10
fov = 120
street = "zstreet"
rownum = 1

try:
    location = str(coordx) + ',' + str(coordy)
    imageName = street + '_' + str(rownum)
    fileName = savePath + imageName + '.jpeg'
    fileUrl = baseUrl + '&heading=' + \
        str(heading) + '&fov=' + str(fov) + '&coordtype=' + \
        coordtype + '&location=' + location

    print(fileUrl)

    print("image exec - " + imageName, end=' : ')
    urllib.request.urlretrieve(fileUrl, fileName)
    print("SUCCESS")
except Exception as e:
    print('ERROR - ', e)
