# func_py_calculate_regular_tetrahedron_volume.py
import math

def func_py_calculate_regular_tetrahedron_volume(edge_length):
    return (edge_length**3 * math.sqrt(2)) / 12

print(func_py_calculate_regular_tetrahedron_volume(6))
