def greet(name, /, gender, *, height, age):
    print(f'我是{name},身高:{height},性别:{gender},年龄{age}')


###################### 正确 ######################
greet('张三', '男', age=18, height=150)
greet('张三', gender='男', age=15, height=150)

##################### 错误 #######################
greet(name='张三', gender='男', age=15, height=150)
greet('张三', '男', 15, height=150)
