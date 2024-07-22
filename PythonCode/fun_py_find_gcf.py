# fun_py_find_gcf.py
def fun_py_find_gcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(fun_py_find_gcf(24, 36))
