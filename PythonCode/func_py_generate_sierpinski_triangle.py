# func_py_generate_sierpinski_triangle.py
import matplotlib.pyplot as plt

def func_py_generate_sierpinski_triangle(iterations):
    def midpoint(p1, p2):
        return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

    vertices = [[0, 0], [1, 0], [0.5, 0.866]]
    x, y = [0.5], [0.5]
    
    for _ in range(iterations):
        chosen_vertex = random.choice(vertices)
        x.append(midpoint([x[-1], y[-1]], chosen_vertex)[0])
        y.append(midpoint([x[-1], y[-1]], chosen_vertex)[1])
    
    plt.scatter(x, y, s=1)
    plt.show()

func_py_generate_sierpinski_triangle(10000)
