import telegram
import os
import time

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)


def main():
    last_update = bot.getUpdates()[-1]
    last_update_id = last_update.update_id

    while True:
        curr_update = bot.getUpdates()[-1]
        curr_update_id = curr_update.update_id
        
        if curr_update_id != last_update_id:
            chat_id = curr_update.message.chat.id
            text = curr_update.message.text
            bot.sendMessage(chat_id, text)

            last_update_id = curr_update_id

        time.sleep(1)

main()