from app import app as flask_app
import pytest


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_hello(client):
    """Test the / route."""
    response = client.get('/')

    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data
