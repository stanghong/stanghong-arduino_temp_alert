# Arduino Temperature Alert

This project monitors temperature using an Arduino and a MAX6675 thermocouple sensor. When the temperature exceeds a set threshold, the Arduino sends a signal to a Python script running on your computer. The script then triggers an IFTTT webhook to send a notification (or SMS) to your phone.

## Features
- Real-time temperature monitoring with Arduino
- LED indicator for high temperature
- Python script listens to Arduino serial output
- Sends notifications via IFTTT (push or SMS)
- Environment variables managed with `.env` file

## Hardware Requirements
- Arduino board (Uno, Nano, etc.)
- MAX6675 thermocouple sensor
- LED and resistor
- USB cable for Arduino

## Software Requirements
- Python 3
- `pyserial`, `requests`, `python-dotenv` packages
- IFTTT account and applet

## Setup
1. **Clone this repository:**
   ```bash
   git clone https://github.com/stanghong/stanghong-arduino_temp_alert.git
   cd stanghong-arduino_temp_alert
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file:**
   ```env
   IFTTT_KEY=your_ifttt_webhook_key
   SERIAL_PORT=your_arduino_serial_port
   ```
4. **Upload the Arduino code to your board.**
5. **Set up your IFTTT applet:**
   - Trigger: Webhook event `temp_alert`
   - Action: Notification or SMS
6. **Run the Python script:**
   ```bash
   python temp_alert.py
   ```

## How it Works
- The Arduino reads temperature and prints status to the serial port.
- If the temperature exceeds the threshold, it prints `ALERT_HIGH_TEMP`.
- The Python script listens for this message and triggers the IFTTT webhook.
- IFTTT sends a notification or SMS to your phone.

## License
MIT 