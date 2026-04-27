age = int(input('请输入年龄'))
has_report = input('您是否提交了体检报告？(是/否)')
level = int(input('请输入你的会员等级(1/2/3)'))

if 18 <= age <= 45:
    print('你的年龄符合比赛要求')
    if has_report == '是':
        print('您已提交体检报告')
        print('您可以参加比赛')
        if level == 1:
            print(f'尊敬的{level}会员，比赛结束后，您可以领取T恤一件')
        elif level == 2:
            print(f'尊敬的{level}会员，比赛结束后，您可以领取跑鞋一双')
        elif level == 3:
            print(f'尊敬的{level}会员，比赛结束后，您可以领取耳机一个')
        elif has_report == '否':
            print(f'您输入的会员等级不正确')
    elif has_report == '否':
        print(f'未提交体检报告，无法参赛')
    else:
        print(f'您输入的提交报告有误')
else:
    print(f'抱歉，年龄不符')
