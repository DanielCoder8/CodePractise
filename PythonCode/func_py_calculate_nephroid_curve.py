# func_py_calculate_nephroid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_nephroid_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * (3 * np.cos(t) - np.cos(3 * t))
    y = a * (3 * np.sin(t) - np.sin(3 * t))
    plt.plot(x, y)
    plt.title("Nephroid Curve")
    plt.show()

func_py_calculate_nephroid_curve(5, 1000)
