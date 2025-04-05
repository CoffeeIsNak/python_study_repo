from timeit import timeit

class MyList:
    def __init__(self, data):
        self._data = data
    def __len__(self):
        return len(self._data)

builtin = list(range(1000))
custom = MyList(list(range(1000)))

print(timeit("len(builtin)", globals=globals()))  # 0.046166300075128675
print(timeit("len(custom)", globals=globals()))  # 0.10982339992187917
