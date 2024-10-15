from flask import request, jsonify
import time
import logging
from app.bot import send_telegram_message

# Initialize logger and bot
logger = logging.getLogger(__name__)
last_heartbeat = time.time()


def receive_heartbeat():
    global last_heartbeat
    data = request.get_json()
    last_heartbeat = time.time()
    message = f"Heartbeat received from {data.get('device_id')} at {time.ctime(last_heartbeat)}"
    send_telegram_message(message)
    return jsonify({'status': 'success'}), 200
