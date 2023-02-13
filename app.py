# deploy bot with flask
from flask import Flask, jsonify, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from bot import start, help, dog, cat
from telegram import Update, Bot
import os

# run ngrok
# ngrok http 5000

TOKEN = os.environ['TOKEN']

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook('https://python2022g.pythonanywhere.com/api/')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/api/', methods=['POST'])
def api():
    print('ok')
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.regex('dog'), dog))
    dispatcher.add_handler(MessageHandler(Filters.regex('cat'), cat))

    dispatcher.process_update(update)
    return jsonify({'ok': True})
        