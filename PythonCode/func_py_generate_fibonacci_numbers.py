# func_py_generate_fibonacci_numbers.py
def func_py_generate_fibonacci_numbers(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print(func_py_generate_fibonacci_numbers(10))
