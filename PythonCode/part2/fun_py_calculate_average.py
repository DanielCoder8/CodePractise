# fun_py_calculate_average.py

def fun_py_calculate_average(lst):
    return sum(lst) / len(lst)

def test_calculate_average():
    numbers = [10, 20, 30, 40, 50]
    print(f"Average: {fun_py_calculate_average(numbers)}")

if __name__ == "__main__":
    test_calculate_average()
