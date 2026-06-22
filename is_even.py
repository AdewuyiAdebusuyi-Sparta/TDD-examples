#---------------------------------TESTS---------------------------------
def test_is_even_one():
    result = is_even(1)
    expected = False
    assert result == expected
def test_is_even_two():
    result = is_even(2)
    expected = True
    assert result == expected
def test_is_even_zero():
    result = is_even(0)
    expected = True
    assert result == expected
def test_is_even_negative():
    result = is_even(-3)
    expected = False
    assert result == expected
def test_is_even_non_int():
    result = is_even("one")
    assert result is None
#---------------------------------FUNCTION---------------------------------

def is_even(num):
    if type(num) != int:
        return None
    return not bool(num % 2)

