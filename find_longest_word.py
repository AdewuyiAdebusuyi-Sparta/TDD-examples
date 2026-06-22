def test_find_longest_word_len_zero_word():
    result = find_longest_word("")
    assert result == ""

def test_find_longest_word_two_words():
    result = find_longest_word("woah", "longer")
    expected = "longer"
    assert result == expected

def test_find_longest_word_three_words():
    result = find_longest_word("woah", "longer", "short")
    expected = "longer"
    assert result == expected

def test_find_longest_word_one_word():
    result = find_longest_word("woah")
    expected = "woah"
    assert result == expected

def test_find_longest_word_is_not_str():
    result = find_longest_word(1, 2, 3)
    assert result is None

def test_find_longest_word_mixed_types():
    result = find_longest_word("woah", 2, "obnoxious")
    expected = "obnoxious"
    assert result == expected
def test_find_longest_word_incorrect_format():
    result = find_longest_word("woah there", 2, "obnoxious maybe")
    expected = "obnoxious"
    assert result == expected

def find_longest_word(*words):
    longest_word = []
    word_list = filter_words(words)

    for word in word_list:
        if len(longest_word) == 0:
            longest_word.append((word))
            continue
        if len(longest_word[0]) < len(word):
            longest_word.clear()
            longest_word.append(word)

        elif (len(longest_word[0]) == len(word) and len(longest_word) > 0):
            longest_word.append(word)
    if len(longest_word) == 1:
        longest_word = longest_word[0]

    if longest_word == []:
        return None

    return longest_word

def filter_words(words):
    new_words = []
    for word in words:
        if type(word) != str:
            continue
        elif " " in word:
            for item in word.split():
                new_words.append(item)
        else:
            new_words.append(word)
    return new_words
