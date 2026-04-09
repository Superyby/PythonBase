# 将指定数据转换为字符串
result1 = str(15)
print(type(result1))

result2 = str(71.3)
print(type(result2))

result3 = str(1.3e5)
print(type(result3))

result4 = str(10_000)
print(type(result4))

# 将指定数据转换为整形(小数直接舍弃，不会四舍五入)
int1 = int(15.6)
int2 = int('71')
int3 = int(' 71 ')
int4 = int(50)
print(type(int1),int1)
print(type(int2))
print(type(int3))
print(type(int4))


f1 = float(15)
f2 = float('15.6')
f3 = float('   5.6   ')
f4 = float(10.1)
f5 = float('50')
print(type(f1))
print(type(f2))
print(type(f3))
print(type(f4))
print(type(f5))