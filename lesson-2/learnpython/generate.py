class counter:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    def get_next(self):
        s = self.start
        print(s)
        print(self.end)
        if(self.start < self.end):
            self.start += 1
        else:
            raise StopIteration

        return s


# c = counter(1, 5)
# iterator = iter(c.get_next, 8)
# print(type(iterator))
# for i in iterator:
#     print(i)


class Container:
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def __iter__(self):
        return iter(ContainerIterator(self))

    def generator(self):
        for item in self._data:
            yield item


class ContainerIterator:
    def __init__(self, c):
        self._container = c

    def __getitem__(self, item):
        if item < len(self._container._data):
            s = self._container._data[item]

            return s

        raise StopIteration

c = Container()
for i in c:
    print(i)

for i in c:
    print(i)

for i in c.generator():
    print(i)

for i in c.generator():
    print(i)