import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "Test Description"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert "id" in response.json()

def test_get_items():
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item():
    # First create an item
    create_response = client.post(
        "/api/v1/items/",
        json={"name": "Test Item", "description": "Test Description"}
    )
    item_id = create_response.json()["id"]
    
    # Then get it
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id
