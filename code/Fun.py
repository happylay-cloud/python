import random

# 定义函数：随机数的产生
'''
格式：
def 函数名([参数,参数...]):
    函数体(重复的代码)
'''


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


print(generate_random)  # 打印函数名

# 调用：函数名（）
generate_random()


# 求随机数的函数
def generate_random(number):
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran)


# 调用
generate_random(2)


def add(a, b):
    result = a + b
    print(result)


add(1, 2)


# 可变参数：定义方式
def add(*args):
    print(args)  # 空元组
    sum1 = 0
    if len(args) > 0:
        for i in args:
            sum1 += i
        print('累加和，sum', sum1)
    else:
        print('没有元素可计算，sum', sum1)


add()
add(1, 2, 3)


# 可变参数：定义方式
def add(name, age, *args):
    print(name, age, args)  # 空元组
    sum1 = 0
    if len(args) > 0:
        for i in args:
            sum1 += i
        print('累加和，sum', sum1)
    else:
        print('没有元素可计算，sum', sum1)


add('华为', '18', 1, 2, 3)


# 关键词参数：key=value
def add1(a, b=10, c=20):  # 关键字参数，此时的b就是默认值
    result = a + b + c
    print(result)


add1(5)

add1(5, 5)

add1(5, c=30)


# 关键词参数
def func(**kwargs):
    print(kwargs)


# 调用
func(a=1, b=2, c=3)


# **persons 装包
def print_boy(name, **persons):
    if isinstance(persons, dict):
        values = persons.values()
        print(values)
        for name, age in values:
            print('{},{}'.format(name, age))


students = {'001': ('张艺兴', 18), '002': ('迪丽热巴', 18)}

# **students 拆包
print_boy('happylay', **students)
