import requests
import platform

url = 'http://127.0.0.1:5000/add-app'

mock_data = {
    "app_name": "MockSystem",
    "version": "3.5.9",
    "description": f"Sent from virtual device: {platform.node()}"
}

try:
    response = requests.post(url, json=mock_data)
    print("\n--- Server Response ---")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error connecting to server: {e}")
