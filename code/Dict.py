# 字典

dict1 = {}  # 空字典

dict2 = dict()  # 空字典 list1 = list() 空列表 tuple1 = tuple() 空元组

dict3 = {'id':'123456','name':'happpylay','age':18}
print(dict3)

dict4 = dict([('name','lay'),('age',18)])
print(dict4)

dict4[1] = '1'
print(dict4)

# 模拟数据库
database = []

for i in range(2):
    # 字典存放用户信息
    user = {}
    user['name'] = i
    database.append(user)

print(database)

# 遍历
for key,value in dict4.items():
    print(key,value)

# values 取出字典中所有值,保存到列表中
result = dict4.values()
print(result)

result = dict4.keys()
print(result)

print( 1 in result)













