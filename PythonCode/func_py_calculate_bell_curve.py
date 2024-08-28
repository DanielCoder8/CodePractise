# func_py_calculate_bell_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_bell_curve(mu, sigma, points):
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, points)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    plt.plot(x, y)
    plt.title("Bell Curve")
    plt.show()

func_py_calculate_bell_curve(0, 1, 1000)
