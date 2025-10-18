#  E-Commerce Backend API (FastAPI)

A production-ready **E-Commerce Backend API** built with **FastAPI**, offering a complete backend solution for an online store. It supports **authentication**, **product management**, **shopping cart**, **orders**, **reviews**, and **Stripe payment integration**, following a clean **Router–Service–Repository architecture** with testing using **Pytest**.

---

##  Features

-  **Authentication** – User registration, login, and JWT-based authorization  
-  **Product Management** – CRUD operations for products with SQLAlchemy  
-  **Shopping Cart** – Add/remove items, calculate totals dynamically  
-  **Order Management** – Checkout process and order tracking  
-  **Product Reviews** – Add, edit, and view product reviews  
-  **Stripe Payment Integration** – Secure payments via Stripe API  
-  **Clean Architecture** – Organized into Routers, Services, and Repositories  
-  **Testing** – Unit and integration tests using Pytest  

---

##  Tech Stack

- **Framework:** FastAPI  
- **ORM:** SQLAlchemy  
- **Database:** PostgreSQL / SQLite (for testing)  
- **Validation:** Pydantic  
- **Authentication:** JWT (via PyJWT)  
- **Payments:** Stripe API  
- **Testing:** Pytest  
- **Dependency Management:** Poetry or Pip  

---

## 📂 Project Structure

```bash
ecommerce_backend/
│
├── app/
│ ├── main.py
│ ├── api/
│ │ ├── routers/
│ │ │ ├── auth_router.py
│ │ │ ├── product_router.py
│ │ │ ├── cart_router.py
│ │ │ ├── order_router.py
│ │ │ └── review_router.py
│ │ ├── services/
│ │ │ ├── auth_service.py
│ │ │ ├── product_service.py
│ │ │ ├── cart_service.py
│ │ │ ├── order_service.py
│ │ │ └── review_service.py
│ │ ├── repositories/
│ │ │ ├── user_repository.py
│ │ │ ├── product_repository.py
│ │ │ ├── cart_repository.py
│ │ │ ├── order_repository.py
│ │ │ └── review_repository.py
│ │ ├── models/
│ │ │ ├── user.py
│ │ │ ├── product.py
│ │ │ ├── cart.py
│ │ │ ├── order.py
│ │ │ └── review.py
│ │ ├── schemas/
│ │ │ ├── user_schema.py
│ │ │ ├── product_schema.py
│ │ │ ├── cart_schema.py
│ │ │ ├── order_schema.py
│ │ │ └── review_schema.py
│ │ └── utils/
│ │ ├── auth_utils.py
│ │ └── stripe_utils.py
│ └── tests/
│ ├── test_auth.py
│ ├── test_product.py
│ ├── test_cart.py
│ ├── test_order.py
│ └── test_review.py
│
├── .env
├── requirements.txt
├── README.md

```


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-backend-fastapi.git
   cd ecommerce-backend-fastapi
   ```

2.**Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```
3.**Install dependencies**
```bash

pip install -r requirements.txt

```
4.**Set up environment variables**
```bash

SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30 # Access token expiry time in minutes
REFRESH_TOKEN_EXPIRE_DAYS=7 # Refresh token expiry time in days
STRIPE_PUBLISHABLE_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key

```
5.**Start the FastAPI server**
```bash
uvicorn app.main:app --reload

```
6. ** Running Tests**
   ```bash
   
   pytest -v
   
   ```
