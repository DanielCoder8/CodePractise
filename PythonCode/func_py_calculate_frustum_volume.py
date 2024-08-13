# func_py_calculate_frustum_volume.py
import math

def func_py_calculate_frustum_volume(r1, r2, height):
    return (1/3) * math.pi * height * (r1**2 + r2**2 + r1 * r2)

print(func_py_calculate_frustum_volume(3, 4, 5))
