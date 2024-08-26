# func_py_calculate_hexagonal_prism_surface_area.py
import math

def func_py_calculate_hexagonal_prism_surface_area(side_length, height):
    area_base = 3 * math.sqrt(3) * side_length**2 / 2
    return 2 * area_base + 6 * side_length * height

print(func_py_calculate_hexagonal_prism_surface_area(3, 10))
