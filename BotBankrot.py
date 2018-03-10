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

if __name__ == '__main__':
    port = int(os.getenv('PORT', 80))
    bbot.run(debug=False, port=port, host='0.0.0.0')