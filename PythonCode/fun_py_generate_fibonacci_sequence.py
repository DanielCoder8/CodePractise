# fun_py_generate_fibonacci_sequence.py
def fun_py_generate_fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fun_py_generate_fibonacci_sequence(10))
