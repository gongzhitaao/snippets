from flatten import flatten


def test_flat_number():
    x0 = 0
    x1 = list(flatten(x0))
    assert isinstance(x1, list) and x1[0] == x0


def test_flat_list_1d():
    x0 = [0, 1, 2, 3]
    x1 = list(flatten(x0))
    eq = all(i in x0 for i in x1)
    assert isinstance(x1, list) and eq


def test_flat_list_str():
    x0 = ['abc', 'bcd']
    x1 = list(flatten(x0))
    eq = all(i in x0 for i in x1)
    assert isinstance(x1, list) and eq


def test_flat_list_2d():
    tmp = [[0, 1], [2, 3]]
    x0 = [0, 1, 2, 3]
    x1 = list(flatten(tmp))
    eq = all(i in x0 for i in x1)
    assert isinstance(x1, list) and eq


def test_flat_list_mixed():
    tmp = [[0, 1], [[[2]]], [[3, 4, 5]], ["abc"]]
    x0 = [0, 1, 2, 3, 4, 5, "abc"]
    x1 = list(flatten(tmp))
    eq = all(i in x0 for i in x1)
    assert isinstance(x1, list) and eq
