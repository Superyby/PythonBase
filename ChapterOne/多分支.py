age = int(input(f'请输入你的年龄'))
if age <= 10:
    print(f'你是幼儿')
elif age <= 18:
    print(f'你是青少年')
elif age <= 30:
    print(f'你是青年')
elif age <= 50:
    print(f'你是中年')
elif age <= 60:
    print(f'你是中老年')
else:
    print(f'你是老年')
