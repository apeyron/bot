import os
import telebot
from flask import Flask, request


TOKEN = '210719426:AAFGyWjfVT5eLUC1DnPmTS1iJkuL-FpOeP4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://botbankrot.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == '__main__':
	bot.polling(none_stop=True)