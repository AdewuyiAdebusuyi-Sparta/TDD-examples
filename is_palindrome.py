import math
def test_ip_not_palindrome():
    actual = is_palindrome("What day is it")
    assert actual == False
def test_ip_is_palindrome_word():
    actual = is_palindrome("Kayak")
    assert actual == True
def test_ip_is_palindrome_sentence():
    actual = is_palindrome("Go hang a salami, I'm a lasagna hog.")
    assert actual == True
def test_ip_is_palindrome_blank():
    actual = is_palindrome(2)
    assert actual == False
def is_palindrome(text):
    if type(text) != str:
        return False
    text = str(text)
    text = text.lower()
    text_temp = ""
    for char in text:
        if char in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            text_temp = text_temp + char
    text = text_temp
    return text == text[::-1]