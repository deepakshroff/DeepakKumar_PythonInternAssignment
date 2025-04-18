import platform
import psutil
import time

print("Booting virtual Android environment...")
time.sleep(1)

# Mock installation
print("Installing sample app (mock)...")
time.sleep(1)
print("App installed successfully!")

# System Info
print("\n--- Virtual System Info ---")
print(f"OS Version: {platform.platform()}")
print(f"Device Model: Android_Virtual_Device_X")
print(f"Available Memory: {round(psutil.virtual_memory().available / (1024 * 1024), 2)} MB")