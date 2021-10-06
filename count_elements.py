def test():
    assert count_elements([1, 2, 3, 3, 2, 1]) == {1: 2, 2: 2, 3: 2}
    assert count_elements([1, 2, 3, 4, 4, 4]) == {1: 1, 2: 1, 3: 1, 4: 3}
    assert count_elements([1, 1, 1]) == {1: 3}
    assert count_elements([1]) == {1: 1}
    assert count_elements([]) == {}
    assert count_elements("abracadabra") == {"a": 5, "b": 2, "c": 1, "d": 1, "r": 2}


def count_elements(array):
    pass
