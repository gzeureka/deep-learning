# 变量定义
# 变量无类型
a = 12
print(a)
print(type(a))

a = 1.3
print(a)
print(type(a))

a = True
print(a)
print(type(a))

# 整数运算
a = 12 + 5 * 4
print(a)
print(a / 5)
print(a // 5)
print(a % 5)

# 浮点数运算
a = 12. + 4.5 * 2.7
print(a)
print(a / 5)
print(a // 3.5)
print(a % 3.5)

# 逻辑运算
print(True)
print(False)
print(not True)
print(not False)
print(True and False)
print(True or False)

# 数字布尔运算
print(2 and 1)
print(0 or -2)
print(-2 and 0)

# 复杂逻辑表达式
print(2 != 1 and not (3 == 2))
print(3 > 2 > 1)

a = None
print(a)
print(type(a))
print(a is None)
print(None is None)

# 变量相当于引用，变量指向的值有类型
# 一切都是对象（重点）
print(isinstance(1, int))
print(isinstance(1, object))
print(isinstance(1., float))
print(isinstance(1., object))
print(isinstance(True, bool))
print(isinstance(True, object))
print(isinstance(None, object))
