import math, pytest

#assert -> statment to test -> output
def test_sqrt():
    num = 49
    assert math.sqrt(num) == 7

def testsquare():
    num = 7
    assert 7*7 == 49

def testequality():
    assert 10 == 10

def test_is_greater():
    assert 30 > 15

@pytest.mark.parametrize('x, y, expected', [(2, 4, 6), (3, 4, 7), (9, 2, 11)])
def test_do_maths(x, y, expected):
    assert do_maths(x, y) == expected

def do_maths(x, y):
    return x + y

