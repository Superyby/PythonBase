num1 = 0b11001
print(num1)
num2 = 0o1034
print(num2)
num3 = 0x1cf
print(num3)

# bin()
result = bin(25)
result1 = oct(540)
result2 = hex(25)
print(result, result1, result2)

v1 = int(result, 2)
v2 = int(result1, 8)
v3 = int(result2, 16)
print(v1, v2, v3)
