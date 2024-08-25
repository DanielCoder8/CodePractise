# func_py_find_twin_primes.py
def func_py_find_twin_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    return [(p, p+2) for p in range(2, limit) if is_prime(p) and is_prime(p+2)]

print(func_py_find_twin_primes(100))
