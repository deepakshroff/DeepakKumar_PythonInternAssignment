import requests
import platform
import uuid
import psutil
import time

# Simulated system info
device_info = {
    "device_id": str(uuid.uuid4()),
    "os_version": platform.platform(),
    "device_model": "Android_Virtual_Device_X",
    "available_memory_mb": round(psutil.virtual_memory().available / (1024 * 1024), 2)
}

print("\n Connecting to backend server...")
time.sleep(1)

try:
    response = requests.post(
        url='http://127.0.0.1:5000/add-app',
        json={
            "app_name": f"VirtualDevice-{device_info['device_id'][:6]}",
            "version": device_info['os_version'],
            "description": f"Model: {device_info['device_model']}, RAM: {device_info['available_memory_mb']} MB"
        }
    )

    print("\n Data sent to server.")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

except Exception as e:
    print(" Failed to connect to server.")
    print(f"Error: {e}")