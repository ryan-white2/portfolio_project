import pytest
from src import create_app
from src.models import User


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture(scope='module')
def new_user():
    test_user = User('Joe Jackson', 'joe@yahoo.com', 7708845654, 'United States', 'M',
                     'Spanish', '1', '1988-06-11', 33, '2009-04-11 11:24:22 UTC', 'jjackson', 'notsecure')
    return test_user
