import random

name = 'happy'
# id() 查看内存地址
print(id(name),name)

name = 'lay'
print(id(name),name)

# 扩展后赋值符号 += -= *= /=


a = 16
b = 3
c =2

# + 加
print(a + b)

# - 减
print(a - b)

# * 乘
print(a * b)

# / 除
print(a / b)

# ** 幂次方
print(b ** c)

# // 取整
print(a // b)

# % 取余
print(a % b)

# 三元表达式：真结果 if 表达式 else 假结果
a = 1
b = 2
result =(a+b) if a<b else (b-a)
print(result)

'''
if else 语句
'''
if a==1:
    print('真')
else:
    print('假')

# 随机数
print(random.randint(1,10))

'''
for 变量名 in 集合:
    语句
'''
# 使用系统给定range()完成范围指定
print(range(8))  # 包含0不包含8

for i in range(8):
    print(i)