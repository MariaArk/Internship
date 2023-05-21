def multiply_numbers(inputs=None):
    if inputs is None:
        return inputs
    multy = 1
    lab = False
    if type(inputs) == str:
        for i in inputs:
            if i.isdigit():
                multy *= int(i)
                lab = True

    elif type(inputs) == list:
        for i in inputs:
            arg = multiply_numbers(i)
            if arg is not None:
                multy *= arg
                lab = True
    else:
        inputs = str(inputs)
        multy = multiply_numbers(inputs)
        if multy is not None:
            lab = True

    if lab:
        return multy
    else:
        return None


k = multiply_numbers()
print(k)
k = multiply_numbers('ss')
print(k)
k = multiply_numbers('1234')
print(k)
k = multiply_numbers('sssdd34')
print(k)
k = multiply_numbers(2.3)
print(k)
k = multiply_numbers([5, 6, 4])
print(k)