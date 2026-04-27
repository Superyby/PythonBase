def order(num, dish):
    print(f'您:{num}份，{dish}')


order(1, '辣椒炒肉')


#################### 位置参数 #########################
def greet(name, height, age, gender):
    print(f'我是{name},身高:{height},性别:{gender},年龄{age}')


greet('张三', 150, 15, '男')
