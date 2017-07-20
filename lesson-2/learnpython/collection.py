# 列表
l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(l)
l.append(9)
print(l)
l.pop()
print(l)
l.insert(0, -1)
print(l)
l.pop(0)
print(l)
l.extend([30, 32, 30])
print(l)
l.remove(30)
print(l)
del l[-1]
print(l)
del l[-1]
print(l)

try:
    print(l[12])
except IndexError as e:
    print(e)

print(len(l))
print(l[1:4])
print(l[:])

l1 = l
l2 = l[:]
l.pop()
print(l)
print(l1)
print(l2)

print(1 in l)

# 字典
d = {
    'name': 'kinuxroot',
    'age': 20
}

print(d['name'])
print(d['age'])
try:
    print(d['beautiful'])
except KeyError as e:
    print(e)

print(d.get('name'))
print(d.get('beautiful'))
print(d.get('beautiful', False))

print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(d.items())
print(list(d.items()))

# 集合自己看

# 元组：不可变的list
t = (1, 2, 3)
print(t)
