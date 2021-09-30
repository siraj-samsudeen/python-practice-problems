def test():
    assert max_element_with_count([1, 2, 3]) == (3, 1)
    assert max_element_with_count([1, 2, 3, 2]) == (2, 2)
    assert max_element_with_count([1]) == (1, 1)
    assert max_element_with_count([]) == (None, 0)
