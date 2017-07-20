# 函数定义
def add(a, b):
    return a + b

print(add(1, 2))


# 多返回值
def add(la, lb):
    return len(la) + len(lb), la + lb

print(add([1, 2, 3], [4, 5]))
length, result = add([1, 2, 3], [4, 5])
print(length, result)


# 默认参数
def inc(a, b=0):
    return a + b

print(inc(5))
print(inc(5, 3))

# 关键字参数
print(add(la=[1, 2, 3], lb=[4, 5]))
print(add(lb=[1, 2, 3], la=[4, 5]))


# 可变参数
def mySum1(*args):
    sumResult = 0
    for arg in args:
        sumResult += arg

    return sumResult

print(mySum1(0, 1, 2, 4))


# 可变关键字参数
def mySum2(**kwargs):
    args = kwargs.get('args', [])
    initial = kwargs.get('initial', 0)

    sumResult = initial
    for arg in args:
        sumResult += arg

    return sumResult

print(mySum2())
print(mySum2(args=[1, 2, 3, 4]))
print(mySum2(args=[1, 2, 3, 4], initial=20))

# 调用可变参数
inArgs = [1, 2, 3, 4, 5, 6, 7]
print(mySum1(*inArgs))

inArgs = {
    'args': [1, 2, 3, 4, 5, 6, 7],
    'initial': 17
}
print(mySum2(**inArgs))


def specialFunc(*args, name, **kwargs):
    print(args)
    print(name)
    print(kwargs)

specialFunc(30, 40, 50, age=20, name='abc')
quit(0)

msg = 'hello'


# 作用域
def testScope1():
    print(msg)


def testScope2():
    msg = 'world'
    print(msg)


def testScope3():
    global msg
    msg = 'world'
    print(msg)

testScope1()
testScope2()
print(msg)
testScope3()
print(msg)


# 函数内部定义函数
def createPrinter(x):
    def printer():
        print('x is ', x)

    return printer

print(createPrinter(10)())


# 匿名函数
def createIncer(x):
    return lambda y: x + y

incer = createIncer(20)
print(incer(35))


# 高阶函数
def forEach(l, op):
    for itemIndex, item in enumerate(l):
        op(item, itemIndex)


def printer(item, itemIndex):
    print('Item {index}: {value}'.format(index=itemIndex, value=item))

forEach([12, 30, 11], printer)
forEach([20, 22], lambda index, value: print('Item {index}: {value}'.format(index=index, value=value)))
l2 = map(lambda x: x + 2, [20, 21, 22])
print(list(l2))
l3 = filter(lambda x: x > 10, [8, 7, 20, 11, 23, 9])
print(list(l3))

# 复杂列表推导式
l2 = [x + 2 for x in [20, 21, 22]]
print(l2)

l3 = [x for x in [8, 7, 20, 11, 23, 9] if x > 10]
print(l3)