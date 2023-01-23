import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, filters, CallbackContext, CommandHandler, BaseFilter

import requests

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    keyboard = [['dog'], ['cat']]
    update.message.reply_text('welcome to our bot', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))

def help(update: Update, context: CallbackContext):
    update.message.reply_text('how can i help you?')

def cat(update: Update, context: CallbackContext):
    response = requests.get('https://aws.random.cat/meow')
    url = response.json()['file']

    update.message.reply_photo(url)

def dog(update: Update, context: CallbackContext):
    response = requests.get('https://random.dog/woof.json')
    url = response.json()['url']

    update.message.reply_photo(url)


def main():
    # updater
    updater = Updater(TOKEN)

    # dispatcher
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(handler=CommandHandler('start', callback=start))
    dispatcher.add_handler(handler=CommandHandler('help', callback=help))

    # message handler 
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Filters.text('dog'), callback=dog))
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Filters.text('cat'), callback=cat))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()