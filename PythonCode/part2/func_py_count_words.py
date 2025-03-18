# func_py_count_words.py

def func_py_count_words(text):
    return len(text.split())

def test_count_words():
    sentence = "Python is a powerful programming language."
    print(f"Word count: {func_py_count_words(sentence)}")

if __name__ == "__main__":
    test_count_words()
