import re


def count_words(string):
        diction = dict()
        string = string.lower()
        string = re.sub(r'[^\w\s]', '', string)
        string = string.split()
        for i in string:
            if i in diction.keys():
                diction[i] += 1
            else:
                diction[i] = 1
        return diction


g = count_words("A man, a plan, a canal -- Panama")
print(g)
g= count_words("Doo bee doo bee doo")
print(g)