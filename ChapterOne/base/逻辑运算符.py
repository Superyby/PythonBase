# and   or   not

# and 逻辑与:判断两侧的值，是否都为True
# or  逻辑或:判断两侧值，只要有一个为Ture就是True
# not 逻辑非:对一个值进行取反

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(False and 3 / 0)
print()

# and 返回不一定是布尔值，可以返回某个参与计算的值本身
print(2 - 2 and True)
print('' and True)
print(True and 8 / 2)
print(3 + 3 and 3 * 4)

print(7 - 2 or False)
print('你好' or 'Yu')
print(False or 8 / 2)
print(2 - 2 or 3 * 4)

print(not True)
print(not False)
print(not 3 < 2)
print(not 3 > 2)
