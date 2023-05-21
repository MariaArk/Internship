def connect_dicts(dict1, dict2):
    diction = dict()
    sum1, sum2 = 0, 0
    for i in dict1.values():
        sum1 += i
    for i in dict2.values():
        sum2 += i
    for i in dict1.keys():
        if dict1[i] > 10:
            diction[i] = dict1[i]
    for i in dict2.keys():
        if dict2[i] > 10:
            if diction.get(i) is None:
                diction[i] = dict2[i]
            elif sum2 >= sum1:
                diction[i] = dict2[i]
    sort_tup = sorted(diction.items(), key=lambda x: x[1])
    return dict(sort_tup)


r = connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })
print(r)
r = connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })
print(r)
r = connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })
print(r)