import pytest


@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_secondprog(self):
        print("This is my second Program")


    def test_firstprog(self):
        print("This is my first Program")


