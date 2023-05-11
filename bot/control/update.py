from telegram import Bot
from telegram.ext import Dispatcher, PicklePersistence
from telegram.ext import Updater, JobQueue
from bot.control.handlers import handlers
from config import BOT_API_TOKEN, DEBUG


persistence = PicklePersistence(filename="persistencebot")

bot_obj = Bot(BOT_API_TOKEN)


updater = Updater(
    token=BOT_API_TOKEN, workers=1000, use_context=True, persistence=persistence,
)
dp = updater.dispatcher

# add handlers
for handler in handlers[::-1]:
    dp.add_handler(handler)
