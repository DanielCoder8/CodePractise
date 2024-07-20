# func_find_substrings.py
def func_find_substrings(string):
    length = len(string)
    return [string[i:j+1] for i in range(length) for j in range(i, length)]

print(func_find_substrings("abc"))
