import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)

user = bot.getMe()
print(user.first_name)