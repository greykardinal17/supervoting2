import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 5, 7),
    (-1, 1, 0),
],
ids=["first", "second", "third"])
def test_add(a, b, expected):
    assert add(a, b) == expected