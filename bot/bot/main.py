from bot.bot import *
from app.services.api_service import request_chat_gpt

def start(update, context):
    update_message_reply_text(
        update, 
        "Hello! I am AI assistant. How can I help you?"
        )

def chat(update, context):
    message = update.message.text
    response = request_chat_gpt(message)
    update_message_reply_text(update, response)