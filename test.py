import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "welcomme to this project"}

def test_create_user():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "phone_number": "1234567890",
        "address": "Test Address",
        "role": "user",
        "hashed_password": "testpassword123"
    }
    response = client.post("/auth/signup", json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "test@example.com"

def test_create_category():
    category_data = {
        "name": "Electronics",
        "description": "Electronic devices"
    }
    response = client.post("/category/createcategory", json=category_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Electronics"

def test_get_all_categories():
    response = client.get("/category/getcategory")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    product_data = {
        "name": "iPhone 15",
        "description": "Latest smartphone",
        "price": 999,
        "quantity": 10,
        "category_id": 1
    }
    response = client.post("/product/createproduct", json=product_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "iPhone 15"

def test_get_all_products():
    response = client.get("/product/getallproduct")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_order():
    order_data = {
        "total_amount": 999,
        "status": "pending",
        "user_id": "1",
        "product_id": "1"
    }
    response = client.post("/orders/createorder", json=order_data)
    assert response.status_code == 201
    assert "user_id" in response.json()
    assert response.json()["total_amount"] == 999

def test_get_all_orders():
    response = client.get("/orders/getorder")
    assert response.status_code == 200
    assert isinstance(response.json(), list)