import pytest


@pytest.mark.smoke
def test_demo1():

    print("Hello")


def test_demo2():

    print("Morning.....")


@pytest.mark.smoke
def test_demo3():
    print("This is demo3")


def test_CreditcardPayment1():
    print("Amount Paid by Credit Card")


def test_CreditcardIssue():
    print("Card Issued")