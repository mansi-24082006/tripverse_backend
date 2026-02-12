import requests
import time
import subprocess
import os

# Start the server in the background
print("Starting server...")
server_process = subprocess.Popen(
    ["uvicorn", "backend.app.main:app", "--reload", "--port", "8000"],
    cwd="d:/project"
)

# Wait for server to start
time.sleep(5)

BASE_URL = "http://127.0.0.1:8000"

try:
    # 1. Signup
    print("Testing Signup...")
    test_email = f"test_{int(time.time())}@example.com"
    signup_data = {"email": test_email, "password": "password123"}
    response = requests.post(f"{BASE_URL}/signup", json=signup_data)
    print(f"Signup Status: {response.status_code}")
    try:
        print(f"Signup Response: {response.json()}")
    except:
        print(f"Signup Response (Text): {response.text}")

    # 2. Login
    print("\nTesting Login...")
    login_data = {"username": test_email, "password": "password123"}
    response = requests.post(f"{BASE_URL}/login", data=login_data)
    print(f"Login Status: {response.status_code}")
    try:
        token = response.json().get("access_token")
    except:
        print(f"Login Response (Text): {response.text}")
        raise
    print(f"Access Token: {token[:20]}...")

    # 3. Chat
    print("\nTesting Chat Flow...")
    headers = {"Authorization": f"Bearer {token}"}
    
    # Step 1: Starting City
    chat_data = {"message": "Bangalore"}
    response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
    print(f"Chat Response (Step 1): {response.json().get('reply')}")

    # Step 3: Days
    chat_data = {"message": "5"}
    response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
    print(f"Chat Response (Step 3): {response.json().get('reply')}")

    # Step 4: Vibe
    chat_data = {"message": "adventure"}
    response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
    print(f"Chat Response (Step 4): {response.json().get('reply')}")

    # Step 5: Budget
    chat_data = {"message": "moderate"}
    response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
    print(f"Chat Response (Step 5): {response.json().get('reply')}")

    # Step 6: People
    chat_data = {"message": "2"}
    response = requests.post(f"{BASE_URL}/chat", json=chat_data, headers=headers)
    print(f"Chat Response (Step 6): {response.json().get('reply')}")

    print("\nVerification Complete!")

finally:
    print("\nShutting down server...")
    server_process.terminate()
