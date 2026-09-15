from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "cs-agent-assistant"}

def test_invalid_booking_id_returns_400():
    payload = {
        "booking_id": "INVALID123",
        "customer_message": "I want to cancel my reservation."
    }
    response = client.post("/agent/assist", json=payload)
    assert response.status_code == 400
    assert "Invalid Booking ID format" in response.json()["detail"]
