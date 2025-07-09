# main.py
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/test-ip")
def test_ip():
    logs = []

    # 1️⃣ Trigger a 3-second outbound call
    try:
        logs.append("📡 Starting 3‑second delay call...")
        res = requests.get("https://httpbin.org/delay/3", timeout=10)
        logs.append(f"✅ Delay call status: {res.status_code}")
    except Exception as e:
        logs.append(f"❌ Delay call failed: {e}")

    # 2️⃣ Fetch your public IP via ipify
    try:
        res2 = requests.get("https://api.ipify.org", timeout=5)
        ip = res2.text.strip()
        print(f"Public IP: {ip}")
        logs.append(f"✅ --My public IP is: {ip}")
    except Exception as e:
        logs.append(f"❌ IP fetch failed: {e}")

    # Return a brief summary and include all logs
    summary = "\n".join(logs)
    print(summary)
    return summary.replace("\n", "<br>"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
