# func_py_generate_password.py

import random
import string

def func_py_generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

def test_generate_password():
    print(f"Generated password: {func_py_generate_password()}")

if __name__ == "__main__":
    test_generate_password()
