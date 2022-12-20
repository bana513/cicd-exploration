import pytest

from mypackage.exception import raise_exception


def test_raise_exception():
    with pytest.raises(ZeroDivisionError):
        # This function should raise an exception
        raise_exception()
