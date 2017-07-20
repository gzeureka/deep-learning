# 基本字符串
a = 'dependency'
print(a)
print(type(a))

print(a[0])
print(type(a[0]))

# 切片
print(a[1:3])
print(a[:3])
print(a[1:])
print(a[:])
print(a[:-1])
print(a[:-2])
print(a[-1:])
print(a[-2:])
print(a[1:5:2])
print(a[5:1:-1])
print(a[5:1:-2])

print('hello ' + 'world')
name = 'kinuxroot'
age = 30
# 2.x格式化
print('my name is: %s' % name)
print('name: %s; age: %d' % (name, age))
print('name: %(name)s; age: %(age)d' % {'name': name, 'age': age})
# 3.x格式化
print('my name is: {}'.format(name))
print('name: {}; age: {}'.format(name, age))
print('age: {1}; name: {0}'.format(name, age))
print('age: {age}; name: {name}'.format(name='kinuxroot', age=20))

