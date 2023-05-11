from bot.bot import *
from app.services.api_service import request_chat_gpt

def start(update, context):
    bot_send_chat_action(update, context)
    update_message_reply_text(
        update, 
        "Hello! I am AI assistant. How can I help you?"
        )

def chat(update, context):
    bot_send_chat_action(update, context)
    message = update.message.text
    job_queue = context.job_queue
    job_queue.run_once(callback=send_response, when=0, context=(update.message.chat.id, message))

def send_response(context):
    # Retrieve the chat ID and message text from the job context
    chat_id, message_text = context.job.context

    # Send the delayed response
    response = request_chat_gpt(message_text)
    context.bot.send_message(chat_id=chat_id, text=response)
