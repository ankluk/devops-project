from app import app as flask_app  # Import our main app
import pytest

# Create a "client" to make virtual requests to our app
@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

# This is our test case
def test_hello(client):
    """Test the / route."""
    # 'client.get' makes a virtual web request to the '/' URL
    response = client.get('/')
    
    # 'assert' checks if a condition is true.
    # We check if the data returned contains our 'Hello' string.
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data
