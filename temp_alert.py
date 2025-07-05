import serial
import time
import requests
from dotenv import load_dotenv
import os

# ====== LOAD ENV ======
load_dotenv()

# ====== CONFIG ======
IFTTT_KEY = os.getenv("IFTTT_KEY")     # Loaded from .env
IFTTT_EVENT = "temp_alert"              # Must match your IFTTT applet event name
SERIAL_PORT = os.getenv("SERIAL_PORT")  # Loaded from .env
BAUD_RATE = 9600

def send_ifttt_notification():
    url = f"https://maker.ifttt.com/trigger/{IFTTT_EVENT}/with/key/{IFTTT_KEY}"
    data = {"value1": "🔥 High temperature detected!"}
    try:
        r = requests.post(url, json=data)
        if r.status_code == 200:
            print("✅ IFTTT alert sent successfully.")
        else:
            print(f"⚠️ IFTTT request failed: {r.status_code} {r.text}")
    except Exception as e:
        print("❌ Error sending request:", e)

def listen_serial():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"📡 Listening to Arduino on {SERIAL_PORT}")
        time.sleep(2)  # wait for Arduino reset

        while True:
            line = ser.readline().decode().strip()
            if line:
                print("🔁 Arduino says:", line)
                if "ALERT_HIGH_TEMP" in line:
                    send_ifttt_notification()
                    time.sleep(10)  # avoid duplicate alerts
                # Temporary test: trigger on any temperature reading
                elif "Current Temp:" in line and "Above threshold" in line:
                    print("🔥 Test: Triggering notification on temperature reading")
                    send_ifttt_notification()
                    time.sleep(10)  # avoid duplicate alerts
    except serial.SerialException:
        print(f"❌ Cannot open serial port {SERIAL_PORT}. Is the Arduino connected?")
    except KeyboardInterrupt:
        print("\n👋 Exiting...")

if __name__ == "__main__":
    listen_serial() 