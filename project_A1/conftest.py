import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Start extended_test main page")
    yield
    print("Finish extended_test main page")