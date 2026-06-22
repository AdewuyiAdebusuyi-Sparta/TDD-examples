from unittest import result


def test_fen_non_numbers():
    result = filter_even_numbers()
    expected = []
    assert result == expected

def test_fen_odd_and_even():
    result = filter_even_numbers(1, 2, 3, 4, 5, 6, 7, 8)
    expected = [2, 4, 6, 8]

def test_fen_odd_all():
    result = filter_even_numbers(1, 3, 5)
    expected = []
    assert result == expected

def test_fen_negative():
    result = filter_even_numbers(-1, -3, -5, -10, -12)
    expected = [-10, -12]
    assert result == expected

def test_fen_string_and_num():
    result = filter_even_numbers(2 ,3, 4, "six", 10, 11)
    expected = [2, 4, 10]
def filter_even_numbers(*nums):
    filtered_list = []
    for num in nums:
        if type(num) != int:
            continue
        if num % 2 != 0:
            continue
        filtered_list.append(num)
    return filtered_list