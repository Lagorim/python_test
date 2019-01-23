import pytest
from Fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminated)
    return fixture