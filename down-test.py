import urllib
import urllib2
import re

savePath = "/Users/Meteor/Downloads"  # 保存路径

# url
baseUrl = 'http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512&fov=180'
coordtype = "bd09ll"
coordx = "116.313393"
coordy = "40.04778"
heading = "180"

try:
    location = coordx + ',' + coordy
    name = street + '_' + str(rownum)
    fileName = savePath + name + '.jpeg'
    fileUrl = baseUrl + '&' + coordtype + '&' + location + '&' + heading

    print ("image exec - " + name, end=' ')
    urllib.urlretrieve(fileUrl, fileName)
    print ("SUCCESS")
except Exception,e:
    print (str(e))
