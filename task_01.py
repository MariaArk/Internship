import re


def is_palindrome(string):
    if string is None:
        return False
    string = str(string)
    string = string.lower()
    string = re.sub(r'[^\w]', '', string)
    size = len(string)
    for i in range(size // 2):
        dk = size - 1 - i
        if string[i] != string[dk]:
            return False
    return True


f = is_palindrome("A man, a plan, a canal -- Panama")
print(f)
f = is_palindrome("Madam, I'm Adam!")
print(f)
f = is_palindrome('333')
print(f)
f = is_palindrome(None)
print(f)
f = is_palindrome("Abracadabra")
print(f)
