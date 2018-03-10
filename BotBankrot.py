import telebot
import random
import os
from flask import Flask, request
import request
from telebot import types

hi = ["Hello", "Hi", "hi", "Привет"]
TOKEN = '210719426:AAFGyWjfVT5eLUC1DnPmTS1iJkuL-FpOeP4'

bbot = telebot.TeleBot(TOKEN)

@bbot.message_handler(commands=['start'])
def keyb(message):
    k = types.ReplyKeyboardMarkup()
    k.row('1', '2', '3')
    bbot.send_message(message.chat.id, "Выберите пункт", reply_markup=k)

@bbot.message_handler(content_types=)


""""@bbot.message_handler(commands=["start"])
def start(message):
    bbot.send_message(message.chat.id, "Ты с нами " + message.chat.first_name)
"""

@bbot.message_handler(content_types=["text"])
def main(message):
    if message.text in hi:
        bbot.send_message(message.chat.id, random.choice(hi))
    else:
        #message.text != "Hi":
        bbot.send_message(message.chat.id, "Не понятно...")

		
# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://botbankrot.herokuapp.com/bot") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)