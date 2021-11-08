import pytest

@pytest.mark.skip
def test_secondProg():
    msg = "HI"
    assert msg in "HI Good Morning", "Strings doesnt match"


@pytest.mark.regression
def test_firstprog1():
    print("This is regression Test")