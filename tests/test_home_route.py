import pytest
from phase3.app import create_app  # Adjusted import

@pytest.fixture
def app():
    # Rename the variable to avoid shadowing the function name
    application = create_app()
    application.config.update({
        "TESTING": True,
    })
    return application

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
