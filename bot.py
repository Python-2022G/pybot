import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)

updates = bot.getUpdates()
last_update = updates[-1]

print(last_update.message.text)