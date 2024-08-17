# func_py_find_cuban_primes.py
def func_py_find_cuban_primes(limit):
    cuban_primes = []
    for i in range(1, limit):
        cuban_number = (i**3 - (i - 1)**3) // (i - 1)
        if all(cuban_number % j != 0 for j in range(2, int(cuban_number**0.5) + 1)):
            cuban_primes.append(cuban_number)
    return cuban_primes

print(func_py_find_cuban_primes(1000))
