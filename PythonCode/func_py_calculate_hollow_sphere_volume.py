# func_py_calculate_hollow_sphere_volume.py
import math

def func_py_calculate_hollow_sphere_volume(outer_radius, inner_radius):
    return (4/3) * math.pi * (outer_radius**3 - inner_radius**3)

print(func_py_calculate_hollow_sphere_volume(5, 3))
