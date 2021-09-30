def topten():
    yield 5

value = topten()

print(value.__next__())