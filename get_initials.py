#---------------------------------TESTS---------------------------------
from unittest import result


def test_get_initials_two_names():
    result = get_initials("John Smith")
    expected = "JS"
    assert result
def test_get_initials_is_not_str():
    result = get_initials(2)
    assert result is None
def test_get_initials_empty_str():
    result = get_initials(2)
    assert result is None
def test_get_initials_mlk():
    result = get_initials("Martin Luther King")
    expected = "MLK"
    assert result == expected
def test_get_initials_single_name():
    result = get_initials("Badger")
    expected = "B"
    assert  result == expected
def test_get_initials_lowercase():
    result = get_initials("Martin luther King")
    expected = "MLK"
    assert result == expected
def test_get_initials_double_barreled():
    result = get_initials("Hunter-Lee Smith")
    expected = "HLS"
    assert result == expected

#---------------------------------FUNCTION---------------------------------

def get_initials(name):
    if type(name) != str or len(name) <= 0:
        return None
    next_initial = True
    initials = ""
    for char in name:
        if char == ' ' or char == '-':
            next_initial = True
        elif next_initial:
            next_initial = False
            initials += char;
    return  initials.upper()

    return None

