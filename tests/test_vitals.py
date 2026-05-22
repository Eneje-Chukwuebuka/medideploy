import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_ok_status(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "ok"


def test_vitals_returns_200(client):
    response = client.get("/vitals")
    assert response.status_code == 200


def test_vitals_contains_required_fields(client):
    response = client.get("/vitals")
    data = response.get_json()
    assert "heart_rate" in data
    assert "blood_pressure" in data
    assert "temperature_celsius" in data
    assert "environment" in data


def test_vitals_heart_rate_is_valid(client):
    response = client.get("/vitals")
    data = response.get_json()
    assert isinstance(data["heart_rate"], int)
    assert 40 <= data["heart_rate"] <= 200
