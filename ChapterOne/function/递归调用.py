def welcome(n):
    if n == 0:
        return
    print("Welcome to Python!")
    welcome(n - 1)
welcome(5)