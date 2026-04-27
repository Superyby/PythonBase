for n in range(1, 11):
    print(f'你好,{n}')

for m in 'abcde':
    print(m)

text = input('输入要加密的文字')
secret = ''
for t in text:
    unicode = ord(t)
    secret += chr(unicode + 1)
print(secret)
