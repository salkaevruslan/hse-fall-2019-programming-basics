import pytest
from division import division


def test_int_result():
    assert division(10, 5) == 2


def test_rational_result():
    assert division(1, 3) == 1/3


def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert division(1, 0)
