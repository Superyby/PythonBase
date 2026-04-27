for day in range(1, 5):
    print('吃饭')
    continue
    print('睡觉')

for day in range(1, 5):
    if day == 2:
        continue
    print('你好')

for day in range(1, 5):
    print(f'第{day}天')
    print('吃饭')
    for item in range(1, 3):
        print('面包')
        continue
        print('banana')
    print('ok')
