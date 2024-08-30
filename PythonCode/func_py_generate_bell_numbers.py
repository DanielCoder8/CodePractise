# func_py_generate_bell_numbers.py
def func_py_generate_bell_numbers(limit):
    bell_numbers = [[1]]
    for n in range(1, limit):
        bell_numbers.append([bell_numbers[-1][-1]])
        for k in range(n):
            bell_numbers[-1].append(bell_numbers[-1][-1] + bell_numbers[-2][k])
    return [b[-1] for b in bell_numbers]

print(func_py_generate_bell_numbers(10))
