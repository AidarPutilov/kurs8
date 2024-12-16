import requests
from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


def send_telegram_message(chat_id, text):
    """Отправка сообщения в Телеграм по chat_id."""

    params = {
        "text": text,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
