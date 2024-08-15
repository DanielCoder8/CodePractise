# func_py_calculate_hyperbolic_cosine.py
import math

def func_py_calculate_hyperbolic_cosine(x):
    return (math.exp(x) + math.exp(-x)) / 2

print(func_py_calculate_hyperbolic_cosine(2))
