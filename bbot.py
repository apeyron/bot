# -*- coding: utf-8 -*-   
import telebot
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

bbot.polling(none_stop=True)