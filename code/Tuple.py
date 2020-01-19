# 元组
import random

t1 = ()

'''
1.定义符号()
2.元组中的内容不可修改
3.关键字 tuple
'''

print(type(t1))

# 注意要加,号
t2 = ('hello',)
print(type(t2))

t3 = ('hello','world')
print(type(t3))

t4 = (2,3,4,5,6)

list1 = []
for i in range(10):
    ran = random.randint(1,20)
    list1.append(ran)
print(list1)

t5 = tuple(list1)
print(t5)

# 查询：下标index 切片[:]
print(t5)
print(t5[0])
print(t5[-1])
print(t5[0:])
# 最大值
print(max(t5))
# 最小值
print(min(t5))
# 求和
print(sum(t5))
# 求长度
print(len(t5))

print(t5.count(6))
# print(t5.index(6))

# 拆包
t1 =(1,2,3)
a,b,c =t1
print(a,b,c)

a,b,c = (1,2,3)
print(a,b,c)

# 变量个数与元组个数不一致
t1 = (1,2,3,4,5,6)
a,*_,c =t1
print(a,c,_)

a,c,*_ = t1
print(a,c,_)

# *c 代表未知的个数0~n
a,b,*c =t1
print(a,b,c)

print(*[1,2,3])