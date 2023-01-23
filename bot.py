import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, CallbackContext, CommandHandler, BaseFilter

TOKEN = os.environ['TOKEN']

def start(update: Update, context: CallbackContext):
    update.message.reply_text('welcome to our bot')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('how can i help you?')

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text)


def main():
    # updater
    updater = Updater(TOKEN)

    # dispatcher
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(handler=CommandHandler('start', callback=start))
    dispatcher.add_handler(handler=CommandHandler('help', callback=help))

    # message handler 
    dispatcher.add_handler(handler=MessageHandler(filters=filters.Filters.all, callback=echo))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()