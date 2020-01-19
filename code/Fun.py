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


add()
add(1, 2, 3)
