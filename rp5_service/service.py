import requests
import psutil
import time
import json
from dotenv import load_dotenv
import os

load_dotenv()


SERVER_URL = os.getenv('SERVER_URL')
INTERVAL = os.getenv('INTERVAL')

def get_system_info():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    ram_usage = memory.percent
    temperature = psutil.sensors_temperatures()['cpu_thermal'][0][1]
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    return {
        "device_id": "raspberry_pi5",
        "heartbeat": "alive",
        "timestamp": current_time,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "cpu_temperature": temperature,
    }

def send_heartbeat():
    system_info = get_system_info()
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(SERVER_URL, data=json.dumps(system_info), headers=headers)
        if response.status_code == 200:
            print("Heartbeat sent successfully")
        else:
            print(f"Failed to send heartbeat, status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

while True:
    send_heartbeat()
    #print(get_system_info())
    time.sleep(INTERVAL)
