import requests
import time
import json

BASE_URL = "http://127.0.0.1:8000"

def test_full_flow():
    print(f"Starting Flow Test at {time.ctime()}")
    
    test_email = f"test_{int(time.time())}@example.com"
    print(f"User: {test_email}")
    
    try:
        # Signup
        requests.post(f"{BASE_URL}/signup", json={"email": test_email, "password": "password123"})
        # Login
        resp = requests.post(f"{BASE_URL}/login", data={"username": test_email, "password": "password123"})
        token = resp.json().get("access_token")
        headers = {"Authorization": f"Bearer {token}"}
        
        steps = ["Bangalore", "Paris", "7", "adventure", "1000", "2"]
        
        for i, msg in enumerate(steps, 1):
            print(f"\nStep {i}: Sending '{msg}'")
            response = requests.post(f"{BASE_URL}/chat", json={"message": msg}, headers=headers)
            reply = response.json().get("reply")
            print(f"Reply: {reply[:150]}...")
            
        print("\nTest Finished Successfully.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_full_flow()
