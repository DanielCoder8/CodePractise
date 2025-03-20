# func_py_find_max_min.py

def func_py_find_max_min(lst):
    return max(lst), min(lst)

def test_find_max_min():
    numbers = [12, 45, 78, 23, 56, 34]
    max_num, min_num = func_py_find_max_min(numbers)
    print(f"Max: {max_num}, Min: {min_num}")

if __name__ == "__main__":
    test_find_max_min()
