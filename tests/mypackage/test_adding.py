import pytest
from mypackage.adding import add, bad_add


def test_add():
    assert add(4, 5) == 9

@pytest.mark.skip(reason="This test should always fail.")
def test_bad_add():
    assert bad_add(4, 5) == 9
