def huge():
 for i in range(100000):
    yield i*i
abc = huge()
print((next(abc)))
print((next(abc)))
print((next(abc)))