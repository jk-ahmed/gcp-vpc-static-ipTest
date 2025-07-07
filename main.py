from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

def periodic_task():
    while True:
        print("📡 Making outbound request...")
        try:
            response = requests.get("https://httpbin.org/delay/3")  # waits 3 seconds
            print("✅ Response received:", response.status_code)
            response = requests.get("https://api.ipify.org")
            print("✅ My public IP is:", response.text)
        except Exception as e:
            print("❌ Error making request:", e)
        time.sleep(300)  # Wait 5 minutes (300 seconds)

# Start the background task on app startup
@app.before_first_request
def start_background_thread():
    thread = threading.Thread(target=periodic_task)
    thread.daemon = True
    thread.start()

@app.route("/")
def home():
    return "Flask API is running and sending periodic outbound traffic every 5 mins."

