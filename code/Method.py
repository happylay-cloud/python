import random

s = 'happylay'
code = ''
for i in range(4):
    ran = random.randint(0, len(s) - 1)
    code+=s[ran]
print('验证码：'+code)

s1 = 'happylay'

result = 'h' in s1
print(result)

# find('要查找的支付',start,end)
position = s1.find('h')  # 返回值是-1则代表没有找到
print(position)

position = s1.find('A')  # 返回值是-1则代表没有找到
print(position)

url = 'https://www.baidu.com'
# 从右侧检索
p = url.rfind('/')
print(p)

# 切片
filename = url[p+1:]
print(filename)

s2 = 'happy lay !'
# replace(old,new,[max])
s3 = s2.replace(' ','#')
print(s3)

# 编码 encode
msg = '快乐的小绵羊'
# gbk中文 gb2312 简体中文 unicode
result = msg.encode('utf-8')
print(result)

# 解码
result = result.decode('utf-8')
print(result)

# startswith() endswith()

filename = 'happylay.doc'
result = filename.endswith('doc')
print(result)

result = filename.startswith('ha')
print(result)

result = filename.isalpha()
print(result)

result = filename.isdigit()
print(result)

new_str = '-'.join('lay')
print(new_str)

new_str = ' '.join('lay')
print(new_str)

s = ' hello world '
s = s.lstrip()  # 去除字符左侧空格
print(s+'$')

s = s.rstrip()  # 去除字符右侧空格
print(s+'$')

n = s.count(' ')  # count(args) 求字符串中指定args的个数
print(n)

s = s.split(' ')  # 分隔字符串
print(s)

