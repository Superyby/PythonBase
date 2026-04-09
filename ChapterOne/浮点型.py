# 浮点型就是带有小数的数字
weight = 15.1
height = 8.7
price = 100.0

print(price)

# 科学计数法表示
speed_of_sound = 3.14e+2 # 3.14乘10的2次方
print(speed_of_sound)
people_number = 7.8e9 # 7.8乘10的9次方
print(people_number)
distance_sun_earth = 1.496E8 # 1.496乘10的8次方
print(distance_sun_earth)
speed_of_light = 2.998E+8 # 2.998乘10的8次方
print(speed_of_light)


one_ml = 1e-3 # 1的10的-3次方
print(one_ml)
one_mg = 1E-3 # 1的10的-3次方
print(one_mg)


"""--------------------格式化输出--------------------"""
name = '张三'
gender = '男'
age = 25
weight = 70.5

# 只能是字符串之间的拼接
info = '我叫' + name + ',我是' + gender + '生' + '今年' + str(age) + '岁' + '体重' + str(weight) + '公斤'
print(info)

# 写法二，使用占位符
info1 = '我叫%s,我是%s生,今年%d岁,体重%.1f公斤' % (name, gender, age, weight)
print(info1)

# 写法三，使用format方法
info3 = f'我叫{name},我是{gender}生,今年{age}岁,体重{weight:.1f}公斤'
print(info3)

"""--------------------占位符精度控制--------------------"""
# %m.nd   %m.ns    %m.nf

# %m.ns
# m 字符串的最小宽度，位数不够会用空格补全，位数小于字符串长度则不起作用  
# 正数是右对齐，负数是左对齐
name = '张三'   # %4s  补充两个空格  %-4s  补充两个空格  往后补充
gender = '男'
age = 25
weight = 70.56

info4 = '我叫%4s,性别%s,今年%d岁,体重%.1f公斤' % (name, gender, age, weight)
print(info4)

# %.3s 不会补位
info5 = '我叫%3s,性别%s,今年%d岁,体重%.1f公斤' % (name, gender, age, weight)
print(info5)


# m和n可以一起用  比如张三   4.1s 意思就是.1 保留一位（张）  然后4个长度，补三个空格


"""--------------------占位符精度控制（浮点数）--------------------"""
# 精度控制，保留n位小数（默认值为6）不够补充0，截断时会四舍五入 ||||||   m控制整体宽度(整体宽度+小数点+小数宽度) 位数不够空格来补，位数小于整体宽度，则自动失效 正数是右对齐，负数是左对齐
info6 = '我叫%3s,性别%s,今年%d岁,体重%9.1f公斤' % (name, gender, age, weight)
print(info6)

"""--------------------占位符精度控制（整数）一样的，不过不够会在前面补充0--------------------"""