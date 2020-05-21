import pytest

from test import add

def test_add():
    print("Testing add")
    assert add(2, 6) == 8

@pytest.mark.skip()
def test_add_null_skip():
    assert add(0, 0) == 0

@pytest.mark.xfail()
def test_add_one_xfail():
    assert add(1, 1) == 0

@pytest.mark.xfail()
def test_add_one2():
    assert add(1, 1) == 2

def test_div_by_0():
    assert 5/0 == 0