def order(num, dish):
    print(f'您:{num}份，{dish}')


order(1, '辣椒炒肉')


#################### 位置参数 #########################
def greet(name, height, age, gender):
    print(f'我是{name},身高:{height},性别:{gender},年龄{age}')


greet('张三', 150, 15, '男')


################### 关键字参数 ########################
def geeet1(name, height, age, gender):
    print(f'我是{name},身高:{height},性别:{gender},年龄{age}')  # 位置参数必须在关键字参数前面


geeet1('张三', 150, gender='男', age=15)
