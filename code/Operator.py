import random

name = 'happy'
# id() 查看内存地址
print(id(name), name)

name = 'lay'
print(id(name), name)

# 扩展后赋值符号 += -= *= /=


a = 16
b = 3
c = 2

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
result = (a + b) if a < b else (b - a)
print(result)

'''
if else 语句
'''
if a == 1:
    print('真')
else:
    print('假')

# 随机数
print(random.randint(1, 10))

'''
for 变量名 in 集合:
    语句
'''
# 使用系统给定range()完成范围指定
print(range(8))  # 包含0不包含8

for i in range(100):
    if i == 10:
        # 占位符
        pass
        break
    print(i)

# range(开始，结束，步长)
for i in range(1, 20, 5):
    print('--->', i)

for i in range(10):
    if i % 3 == 0:
        # 跳过循环体下方的语句,直接进行下一次循环
        continue
    print('for--->', i)

# while循环
sum_2 = 0
i = 1
while i <= 2:
    sum_2 += i
    i += 1
print(sum_2)

# 逻辑判断
s1 = 1
s2 = 2
print(s1 == s2)
print(s1 != s2)

# in
name = 'happylay'
result = 'h' in name
print(result)

# % 字符串格式化
print('%s' % 'happylay')

# r 保留原格式
print(r'%s说：\n' % name)

# [] [:] range(1,10) --类似-->[1:10]
filename = '0123456'
print(filename[0])
print(filename[0:3])  # 包前不包后
print(filename[3:7])  # 截取字符串

# [3:]省略
print(filename[3:])  # 只要省略的是后面的，表示一直取到字符串的末尾
print(filename[:7])  # 只要省略的是前面的，表示从0开始取值

# [5:-1]负数
print(filename[5:-1])

print(filename[:-1])

print(filename[-2:])

# [::-1]倒叙
print(filename[::-1])

# [start:end:反向和步长]
s1 = 'hello world'
# h e l l o  w o r l d
# 0 1 2 3 4  6 7 8 9 10
print(s1[-1:-6:-1])

print(s1[:5])

print(s1[::-1])

print(s1[4:2:-1])

print(s1[2:-3:1])

print(s1[::2])

print(s1[::-2])