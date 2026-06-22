def test_mci_mixed_items():
    actual = most_common_item("apple", "s", 2, 10.1, "square", "apple")
    expected = "apple"
    assert actual == expected
def test_mci_no_items():
    actual = most_common_item()
    expected = None
    assert  actual == expected

def most_common_item(*items):
    if len(items) <=0:
        return None
    item_count = {}
    for item in items:
        item_count[item] = 0
    for item in items:
        item_count[item] +=1
    return max(item_count, key=item_count.get)