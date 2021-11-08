import pytest


def test_myprog1(myFixture):
    print("This needs to be printed")

@pytest.fixture()
def myFixture():
    print("I will be executed first")
    yield
    print("Last execution")