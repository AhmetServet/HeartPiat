import time
import logging
from config.settings import HEARTBEAT_INTERVAL, WARNING_THRESHOLD
from app.bot import send_telegram_message

logger = logging.getLogger(__name__)
last_heartbeat = time.time()



def monitor_heartbeat():
    global last_heartbeat
    message_id = None
    send_telegram_message("Heartbeat monitoring started...")

    while True:
        time_since_last = time.time() - last_heartbeat
        if time_since_last > WARNING_THRESHOLD:
            message = f"No heartbeat received in the last {time_since_last} seconds!"
            message_id = send_telegram_message(message)

        time.sleep(HEARTBEAT_INTERVAL)

# Entry point for running the monitor independently
#if __name__ == '__main__':
#   monitor_heartbeat()
