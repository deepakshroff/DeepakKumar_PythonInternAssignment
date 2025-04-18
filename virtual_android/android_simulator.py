import platform
import psutil
import time
import uuid

print("\n Booting virtual Android environment...")
time.sleep(1.2)
print(" Virtual Android OS loaded successfully.")

# Simulate app installation
print("\n Installing sample app...")
time.sleep(1)
print(" Sample app installed.")

# Simulated system info
print("\n Retrieving device system info...")
time.sleep(0.8)

device_info = {
    "device_id": str(uuid.uuid4()),
    "os_version": platform.platform(),
    "device_model": "Android_Virtual_Device_X",
    "available_memory_mb": round(psutil.virtual_memory().available / (1024 * 1024), 2)
}

print("\n--- Virtual Device Info ---")
for key, value in device_info.items():
    print(f"{key}: {value}")

print("\n[✔] Virtual Android system simulation complete.")