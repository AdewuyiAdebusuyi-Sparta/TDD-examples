def test_cw_regular_string_upper_vowels():
    result = count_words("The Quick Brown Fox Jumps Over The Lazy Dog")
    expected = {"a":1, "b":1, "c":1, "d":1, "e":3, "f":1, "g":1, "h":2, "i":1, "j":1, "k":1, "l":1, "m":1, "n":1, "o":4, "p":1, "q":1, "r":2, "s":1, "t":2, "u":2, "v":1, "w":1, "x":1, "y":1, "z":1}
    assert result == expected
def test_cw_regular_string_2nd():
    result = count_words("Hi, it's Dewuyi")
    expected = {"a":0, "b":0, "c":0, "d":1, "e":1, "f":0, "g":0, "h":1, "i":3, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":1, "t":1, "u":1, "v":0, "w":1, "x":0, "y":1, "z":0}
    assert result == expected

def test_cw_non_string():
    result = count_words(4)
    expected = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    assert result == expected


def count_words(text):
    word_count = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    word_key = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if type(text) != str:
        return word_count
    text = text.lower()
    for char in text:
        if char not in word_key:
            continue
        word_count[char] +=1
    return word_count