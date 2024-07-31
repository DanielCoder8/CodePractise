# func_py_find_shortest_word.py
def func_py_find_shortest_word(words):
    return min(words, key=len)

print(func_py_find_shortest_word(["short", "longest", "tiny"]))
