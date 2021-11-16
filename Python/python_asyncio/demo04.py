# demo-04, yield and yield from compare

# normal generator
def gen():
    for c in 'AB':
        yield c # single value
    for i in range(1, 3):
        yield i

# yield from version of gen()
def gen2():
    yield from "AB" # with iterable object (iterator, generator)
    yield from range(1, 3)

print(list(gen()))

print(list(gen2())) 