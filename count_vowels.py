def test_cv_regular_string_upper_vowels():
    result = count_vowels("The Quick Brown Fox Jumps Over The Lazy Dog")
    expected = 12
    assert result == expected
def test_cv_regular_string_2nd():
    result = count_vowels("Hi, it's Dewuyi")
    expected = 5
    assert result == expected

def test_cv_non_string():
    result = count_vowels(4)
    expected = 0
    assert result == expected


def count_vowels(text):
    n_o_vowels = 0
    if type(text) != str:
        return n_o_vowels
    text = text.lower()
    for char in text:
        if char in {"a", "i", "e", "u", "o"}:
            n_o_vowels += 1
    return n_o_vowels