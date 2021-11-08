import pytest


@pytest.fixture(scope="class")
def setup():
    print("I m first to be Executed")
    yield
    print("Execution Done")


@pytest.fixture(scope="class")
def dataset():
    print("This data will be transferred to Test Method")
    return ["Vishnu", "Mishra"]


@pytest.fixture(params=[("Chrome", "Vishnu"), ("Firefox", "Hari"), ("IE", "Karan")])
def datasetdynamic(request):
    print("This is all new data which is dynamic in nature")
    return request.param
