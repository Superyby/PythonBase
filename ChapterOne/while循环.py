n = 0
while n < 10:
    print(f'第{n}次你好啊')
    n += 1
    print(f'我+1啦{n}')

print(f'您在迷宫中，请做出选择')
riddle = '你是什么人'
answer = '你的心上人'
guess = ''

while guess != answer:
    print(f'问题:{riddle}')
    # 输入答案
    guess = input()
    if guess == answer:
        print(f'正确')
    else:
        print(f'错误')
