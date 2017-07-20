a = 25
b = 30

# if
if b > a and b > 10:
    print('OK')

if a == 30:
    print('A')
elif b == 40:
    print('B')
else:
    print('C')

# for
for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 1, -2):
    print(i)

d = {
    'name': 'kinuxroot',
    'age': 20,
    'beautiful': True
}

for k in d:
    print(k, d[k])

for k in d.keys():
    print(k, d[k])

for v in d.values():
    print(v)

for k,v in d.items():
    print(k, v)

l = [ 20, 18, 15, 24 ]
for index, value in enumerate(l):
    print(index, value)

for index, (k, v) in enumerate(d.items()):
    print(index, k, v)

l2 = [i * 2 for i in l]
print(l)

c = a if a > b else b
print(c)
