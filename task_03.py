def max_odd(array):
    max = 0
    for i in array:
        if (i is not None) & (type(i) != str):
            if type(i) == list:
                f = max_odd(i)
                if f > max:
                    f = max
            else:
                if (i % 2 != 0) & (i > max):
                    max = i
    if max == 0:
        return None
    return max


b = max_odd([1, 2, 3, 4, 4])
print(b)
b = max_odd([21.0, 2, 3, 4, 4])
print(b)
b = max_odd(['ololo', 2, 3, 4, [1, 2], None])
print(b)
b = max_odd(['ololo', 'fufufu'])
print(b)
b = max_odd([2, 2, 4])
print(b)