import pytest

from ELMOUATASSIM_Mohammed_5_API_flask_072023 import create_app

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

