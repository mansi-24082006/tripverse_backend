# 🌍 Tripverse Backend – FastAPI

Tripverse Backend is a FastAPI-based backend system that powers the Tripverse AI trip planning application.  
It provides authentication, JWT security, and a multi-step trip planning chat flow with persistent storage using SQLite and SQLAlchemy.

---

## 🚀 Features

- ✅ User Signup & Login
- ✅ JWT Authentication
- ✅ Secure Password Hashing (bcrypt)
- ✅ Multi-Step Trip Planning Chat Flow
- ✅ SQLite Database (Auto-Initialized)
- ✅ SQLAlchemy ORM
- ✅ Pydantic Data Validation
- ✅ Interactive Swagger API Documentation

---
## 🏗️ Project Structure

```bash
backend/
│
├── app/
│   ├── main.py          # 🚀 FastAPI entry point & API routes
│   ├── auth.py          # 🔐 JWT authentication & password hashing
│   ├── trip_planner.py  # 🤖 AI trip planning logic (state machine)
│   ├── models.py        # 🗄️ SQLAlchemy ORM models
│   ├── schemas.py       # 📦 Pydantic request/response schemas
│   ├── database.py      # ⚙️ Database configuration & session setup
│
├── requirements.txt     # 📜 Python dependencies
│
└── tripverse.db         # 🗂️ Auto-created SQLite database
```
---

## 🛠️ Tech Stack

- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **Passlib (bcrypt)**
- **python-jose (JWT)**
- **Uvicorn**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/tripverse_backend.git
cd tripverse_backend


### 2️⃣ Install Dependencies

pip install -r backend/requirements.txt


### 3️⃣ Start the Server

uvicorn backend.app.main:app --reload


Server will run at:

http://127.0.0.1:8000


---

## 📘 API Documentation

FastAPI provides automatic interactive API documentation.

Open in your browser:

http://127.0.0.1:8000/docs


You can test:
- Signup
- Login
- Chat endpoints
- JWT Authorization

---

## 🔐 Authentication Flow

1. **Signup** → Register a new user  
2. **Login** → Receive JWT access token  
3. Use token in protected routes:

Authorization: Bearer <your_token>


---

## 💬 Trip Planning Chat Flow

The backend includes a step-based trip planning system.

| Step | Question |
|------|----------|
| 1 | From where will you start your journey? |
| 2 | Where do you want to travel? |
| 3 | How many days is your trip? |

The system:
- Stores user responses
- Maintains chat state
- Automatically transitions to the next step

---

## 🧪 Integration Testing

A verification script `verify_backend.py` tests:

- ✔ Server startup
- ✔ User signup
- ✔ User login
- ✔ JWT validation
- ✔ Full chat flow

Example flow:

Start Location → Bangalore
Destination → Goa
Response → How many days is your trip?


---

## 🗄️ Database

- Database file: `tripverse.db`
- Automatically created on first run
- Stores:
  - Users
  - Hashed passwords
  - Chat progress
  - Trip responses

---

## 📦 Future Improvements

- PostgreSQL support
- AI-based itinerary generation
- Google Maps integration
- Hotel & flight suggestions
- Save & manage multiple trips
- Smart personalized recommendations

---

## 👩‍💻 Author

Developed for **Tripverse AI**

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
Pull requests and contributions are welcome!

