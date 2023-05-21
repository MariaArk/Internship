def coincidence(list=[], range=range(0, 1)):
    arr = []
    minim = range.start
    maxim = range.stop
    for i in list:
        if (i is not None) & (type(i) != str):
            if minim <= i < maxim:
                arr += [i]
    return arr


d = coincidence([1, 2, 3, 4, 5], range(3, 6))
print(d)
d = coincidence()
print(d)
d = coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))
print(d)