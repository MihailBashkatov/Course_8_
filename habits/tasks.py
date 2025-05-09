from celery import shared_task

from habits.services import send_telegram_message
from users.models import User


@shared_task
def send_reminder(email):
    """Task to send Telegram message, if user chose option to get telegram messages"""

    message = 'Hello, world"'
    user = User.objects.get(email=email)
    if user.telegram_chat_id:
        telegram_chat_id = user.telegram_chat_id
        send_telegram_message(telegram_chat_id, message)
