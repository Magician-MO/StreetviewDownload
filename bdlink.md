http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ
&width=1024
&height=512
&coordtype=bd09ll
&location=116.313393,40.04778
&fov=180
&heading=180

http://api.map.baidu.com/panorama/v2?ak=btM7vYlzOF2GPfjR8tHklMziZmXYT8DQ&width=1024&height=512&coordtype=bd09ll&fov=180&heading=180&location=116.313393,40.04778

**服务参数列表**

```
http://api.map.baidu.com/panorama/v2?
```

**组成说明：**

域名：api.map.baidu.com

服务名：panorama

版本号：v2

ak： 该套API免费对外开放，使用前请先申请密钥。申请密钥时，请选择ak的应用类型为 “for server”。

**服务参数说明**

| 参数名    | 必选 | 默认值 | 描述                                                         |
| --------- | ---- | ------ | ------------------------------------------------------------ |
| ak        | 是   | 无     | 用户的访问密钥。只支持浏览器端ak和Android/IOS SDK的ak，服务端ak不支持sn校验方式。 |
| mcode     | 否   | 无     | 安全码。若为Android/IOS SDK的ak, 该参数必需。                |
| width     | 否   | 400    | 图片宽度，范围[10,1024]                                      |
| height    | 否   | 300    | 图片高度，范围[10,512]                                       |
| location  | 是   | 无     | 全景位置点坐标。坐标格式：lng<经度>，lat<纬度>，例如116.313393,40.047783。 |
| coordtype | 否   | bd09ll | 全景位置点的坐标类型，目前支持bd09ll（百度坐标），wgs84ll（GPS坐标）和gcj02（google，高德，soso坐标）。 |
| poiid     | 是   | 无     | poi的id，该属性通常通过place api接口获取，poiid与panoid、location一起设置全景的显示场景，优先级为：poiid>panoid>location。其中根据poiid获取的全景视角最佳。 |
| panoid    | 是   | 无     | 全景图id，panoid与poiid、location一起设置全景的显示场景，优先级为：poiid>panoid>location。 |
| heading   | 否   | 0      | 水平视角，范围[0,360]                                        |
| pitch     | 否   | 0      | 垂直视角，范围[0,90]。                                       |
| fov       | 否   | 90     | 水平方向范围，范围[10,360]，fov=360即可显示整幅全景图        |

**返回码说明**

| 状态码 | 含义                                                    |
| ------ | ------------------------------------------------------- |
| 0      | 正常                                                    |
| 507    | coordtype赋值错误，目前只支持bd09ll,wgs84ll             |
| 509    | ak为必选参数，没有加ak时返回错误。其他ak验证码，请 查看 |
| 508    | 请求ak验证服务失败                                      |
| 302    | 坐标的格式不对，经纬度应该以逗号分隔                    |
| 303    | 百度经纬度坐标转换为百度墨卡托坐标错误                  |
| 304    | wgs84经纬度坐标转换为百度墨卡托坐标错误                 |
| 402    | 请求坐标转panoid服务，返回错误，可能是该点没有panoid    |
| 401    | 请求坐标转panoid服务失败                                |
| 403    | 没有panoid 和 location 参数                             |
| 404    | 根据poi id获取pano id服务请求失败                       |
| 405    | 根据poi id获取pano id服务返回无效的pano id              |
| 501    | 超出了width的范围                                       |
| 502    | 超出了height的范围                                      |
| 503    | 超出了heading 的范围                                    |
| 506    | 超出了fov的范围                                         |
| 601    | 请求街景服务失败                                        |
