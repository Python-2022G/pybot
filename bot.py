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
