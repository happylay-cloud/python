# 声明列表
names = ['jack', 'tom', 'lucy']
print(names)

computer_brands = []
print(id(computer_brands))

# 元素获取
print(names[0])
print(names[1])

# 获取最后一个元素
print(names[-1])
print(names[len(names) - 1])

# 循环
for name in names:
    if name == 'tom':
        print(name)
        break
else:
    print('不存在')

# 简便
if 'tom' in names:
    print('存在')
else:
    print('不存在')

# 改
brands = ['huawei', 'lenove', '支持华为', 'HW']

print(brands)

print(brands[-1])

brands[-1] = 'HuaWei'

print(brands)

for brand in brands:
    if '华为' in brand:
        brand = 'HUAWEI'

print(brands)

for i in range(len(brands)):
    if '华为' in brands[i]:
        brands[i] = 'HUAWEI'
        break
print(brands)

# 删除 del
del brands[1]
print(brands)

len1 = len(brands)
i = 0
while i < len1:
    if 'lenove' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        len1 -= 1
    i += 1
print(brands)

# 切片

list = ['张艺兴','迪丽热巴','何炅']
print(list)

print(list[1:2])

print(list[::-1])

print(list[2:1:-1])

# 增加 append
list.append('杨超越')
print(list)

# 列表合并 extend
list.extend(names)
print(list)

# 列表合并 +
list = list + names
print(list)

# 插入 insert
list.insert(1,'罗志祥')
print(list)

# 求和
list1 =[1,4,2,3]
result = sum(list1)
print(result)

# 排序-默认升序
result = sorted(list1)
print(result)

result = sorted(list1,reverse=True)
print(result)