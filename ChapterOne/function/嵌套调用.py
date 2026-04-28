def speek(msg):
    print("-------------")
    print(msg)
    print("-------------")


def greet(name, msg):
    print("-------------")
    print("Hello, " + name)
    print("-------------")
    speek(msg)


greet("Alice", "Welcome to the world of Python!")
