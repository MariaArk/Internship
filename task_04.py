def sort_list(list):
    if not list:
        return list
    min_ = min(list)
    max_ = max(list)
    for i in range(len(list)):
        if list[i] == min_:
            list[i] = max_
        elif list[i] == max_:
            list[i] = min_
    list += [min_]
    return list



a = sort_list([])
print(a)
a = sort_list([2,4,6,8])
print(a)
a = sort_list([1])
print(a)
a = sort_list([1,2,1,3])
print(a)