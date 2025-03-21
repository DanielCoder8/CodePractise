# fun_py_find_max_in_list.py

def fun_py_find_max_in_list(lst):
    return max(lst)

def test_find_max_in_list():
    numbers = [45, 78, 23, 90, 12]
    print(f"Maximum number: {fun_py_find_max_in_list(numbers)}")

if __name__ == "__main__":
    test_find_max_in_list()
