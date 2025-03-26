# fun_py_calculate_gcd.py

import math

def fun_py_calculate_gcd(a, b):
    return math.gcd(a, b)

def test_calculate_gcd():
    print(f"GCD of 48 and 18: {fun_py_calculate_gcd(48, 18)}")

if __name__ == "__main__":
    test_calculate_gcd()
