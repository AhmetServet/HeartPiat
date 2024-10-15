from telebot import TeleBot
from config.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = TeleBot(token=str(TELEGRAM_BOT_TOKEN))


def send_telegram_message(message):
    bot.send_message(chat_id=str(TELEGRAM_CHAT_ID), text=message)
