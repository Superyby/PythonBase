def greet(name, gender, age, height, msg='你好'):
    print(f'我是{name},身高:{height},性别:{gender},年龄{age}')
    print(f'我想说{msg}')


greet('张三', '男', 15, 150)
greet('张三', '男', 15, 150,'ok')

