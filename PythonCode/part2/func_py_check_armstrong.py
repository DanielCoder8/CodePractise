# func_py_check_armstrong.py

def func_py_check_armstrong(n):
    digits = list(map(int, str(n)))
    return sum(d ** len(digits) for d in digits) == n

def test_check_armstrong():
    numbers = [153, 9474, 9475]
    for num in numbers:
        print(f"{num} is Armstrong: {func_py_check_armstrong(num)}")

if __name__ == "__main__":
    test_check_armstrong()
