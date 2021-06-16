count = 1

def a():
    count = 'a函数里面'
    def b():
        nonlocal count
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__':
    a()
    print(count)





count = 1

def a():
    #nonlocal count    #这种声明方法肯定报错，
    def b():
        nonlocal count    #在a()函数中没有提前声明，所以报错
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__':
    a()
    print(count)


count = 1

def a():
    global count
    count = 'a函数里面'
    def b():
        nonlocal count
        print(count)
        count = 2
    b()
    print(count)

if __name__ == '__main__':
    a()
    print(count)