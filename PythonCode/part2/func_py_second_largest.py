# func_py_second_largest.py

def func_py_second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def test_second_largest():
    numbers = [5, 3, 9, 7, 2, 9, 8]
    print(f"Second largest number: {func_py_second_largest(numbers)}")

if __name__ == "__main__":
    test_second_largest()
