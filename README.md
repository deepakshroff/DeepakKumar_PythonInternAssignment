# Python Intern Assignment - Deepak Kumar

Hi there! 👋

This project contains my submission for the Python Intern Assignment. It includes a Flask API, SQLite database, virtual Android simulator (mocked), and a simple networking script.

## 🚀 How to Run

### Step 1: Setup Environment
```bash
cd app
pip install -r requirements.txt
```

### Step 2: Run API
```bash
python app.py
```

### Step 3: (Optional) Add Sample Data
```bash
python sample_data.py
```

### Step 4: Test API
Use Postman or curl:
```bash
curl -X POST http://127.0.0.1:5000/add-app -H "Content-Type: application/json" -d '{"app_name": "TestApp", "version": "1.0", "description": "Test Description"}'
```

## 🤖 Virtual Android System (Mocked)
```bash
cd ../virtual_android
python android_simulator.py
```

## 🌐 Networking
```bash
cd ../networking
python device_to_server.py
```

Enjoy exploring! 😄
"""