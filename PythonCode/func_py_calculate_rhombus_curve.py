# func_py_calculate_rhombus_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_rhombus_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * np.cos(t)
    y = a * np.sin(t)
    plt.plot(x, y)
    plt.title("Rhombus Curve")
    plt.show()

func_py_calculate_rhombus_curve(5, 1000)
