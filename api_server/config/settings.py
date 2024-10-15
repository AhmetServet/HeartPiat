import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Heartbeat configuration
HEARTBEAT_INTERVAL = 5
WARNING_THRESHOLD = HEARTBEAT_INTERVAL * 1
