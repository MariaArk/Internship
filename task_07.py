def combine_anagrams(words_array):
    arr = []
    for i in words_array:
        array = []
        x = sorted(i.lower())
        for j in words_array:
            y = sorted(j.lower())
            if x == y:
                array += [j]

        if array not in arr:
            arr += [array]

    return arr


z = combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])
print(z)