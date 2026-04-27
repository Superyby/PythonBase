def test3(a, b, *args, c='ok', **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)


test3('张三', '男', '抽烟', '喝酒', c='yu', age=15, height='150')
