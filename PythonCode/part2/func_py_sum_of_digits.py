# func_py_sum_of_digits.py
def func_py_sum_of_digits(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n = n // 10
    return total_sum
