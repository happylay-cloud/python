# 声明集合：set
s1 = set() # 创建空集合，只能使用set()

s2 = {1,2,3}  # 字典{key:value} 集合{元素}

print(type(s1))
print(type(s2))

list1 = [1,2,3,4,5,3,4,5]
s3 = set(list1)
print(s3)

# 增加一个元素
s1.add('hello')
s1.add('lay')
t1 = ('hello','world')
# 添加多个元素
s1.update(t1)
s1.add(t1)
print('--->',s1)

s3.discard(1)
print(s3)

set1 = {1,2,3}
set2 = {2,3,4}

set3 =set2-set1  # 差集 difference()
print(set3)

set5 = set2.difference(set1)
print(set3)

set6 = set2 & set1  # 交集 intersection()
print(set6)

set7 = set2.intersection(set1)
print(set7)

set8 = set2 | set1  # 并集 union()
print(set8)

set9 =set2.union(set1)
print(set9)

# 不可变类型 int str float 元组

# 可变类型 字典dict 列表list