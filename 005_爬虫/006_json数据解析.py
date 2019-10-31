'''
{}：代表对象（字典）
[]：列表
: ：键值对
, ：分割两个部分
'''
import json

jsonStr = '{"name":"dogpi","age":"18","hobby":["play","money","english"],"parames":{"a":1,"b":2}}'

# 将json格式的字符串转为Python数据类型对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])
print(jsonData["parames"]["a"])

# 将Python数据类型对象转为json字符串
jsonData2 = {"name":"dogpi","age":"18","hobby":["play","money","english"],"parames":{"a":1,"b":2}}
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))

# 读取本地的json文件
path1 = r"name.json"
with open(path1) as fd:
    data = json.load(fd)
    print(data)
    print(type(data))

# 写json文件
path2 = r"name_new.json"
with open(path2,'w') as fd:
    json.dump(jsonData2,fd)