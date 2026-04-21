# 等价写法
# age = input('请输入你的年龄')
name = input('请输入你的名字:')
age = input('请输入你的年龄')

print(f'你今年的年龄是{age}')  # age是字符串类型
print(f'你的名字是{name}')
age = int(age)
print(f'你明年的年龄是{age + 1}')  # 字符串无法相加操作，需转换为int
