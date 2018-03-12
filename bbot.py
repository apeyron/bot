# -*- coding: utf-8 -*-   
import telebot
import os
import requests
from bs4 import BeautifulSoup
from telebot import types
hi = ["Hello", "Hi", "hi", "Привет"]

TOKEN = os.environ["TOK"]
NAM = os.environ["NAME"]
data = {'name': 'diaga', 'pass': '00000', 'form_id': 'user_login_block'}
#data["name"] = NAM
print(data)

bbot = telebot.TeleBot(TOKEN)

@bbot.message_handler(commands=['start'])
def keyb(message):
    k = types.ReplyKeyboardMarkup(True, False)
    k.row('Поиск', 'but2', 'info')
    send = bbot.send_message(message.from_user.id, 'Выберите, чем могу быть полезен', reply_markup = k)
    bbot.register_next_step_handler(send, search)

def search(message):
    if message.text == 'Поиск':
        k2 = types.ReplyKeyboardMarkup(True, False)
        k2.row('b1', 'b2', 'back1')
        send = bbot.send_message(message.chat.id, "ВВедите запрос", reply_markup=k2)
        bbot.register_next_step_handler(send, ks)
    elif message.text == 'info':
        send = bbot.send_message(message.chat.id, "but2")
        bbot.send_message(message.chat.id, 'Бот позволяте искать по коммерсанту')
        bbot.register_next_step_handler(send, keyb)
    elif message.text == 'but2':
        send = bbot.send_message(message.chat.id, "Не понятно...")
        bbot.register_next_step_handler(send, keyb)

def back1 (message):
    if message.text == 'b1':
        k3 = types.ReplyKeyboardMarkup(True, False)
        k3.row('bb', 'bbb', 'bbb')
        send = bbot.send_message(message.from_user.id, 'bbbbbb', reply_markup=k3)
        bbot.register_next_step_handler(send, keyb)
    elif message.text == 'back1':
        keyb(message)

def ks (message):
    try:
        url = 'http://ktobankrot.ru'
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)  Safari/537.36'}
        ses = requests.Session()
        # Делаем переход к странице с авторизацией
        rs = ses.get(url)
        # Получение поля form_build_id из формы авторизации
        root = BeautifulSoup(rs.content, 'lxml')
        form_build_id = root.select_one('[name=form_build_id]')
        data['form_build_id'] = form_build_id['value']
        # Авторизация
        rs = ses.post(url, data=data)
        # Поиск
        ss = ses.get(url + '/search?fulltext=' + message.text)
        # print(ss.text)
        rez = BeautifulSoup(ss.text, "html.parser")
        sear = rez.find('div', {'class': 'view-content'})
        items = sear.find_all('div', {'class': 'views-row'})
        # находим ссылки
        for i in items:
            kom_num = i.find('div', {'class': 'views-field views-field-title'}).find('a').text
            kom_date = i.find('div', {'class': 'views-field views-field-field-dop-body'}).find('p').text
            kom_link = i.find('div', {'class': 'views-field views-field-field-url-doc'}).find('a').get('href')
            bbot.send_message(message.chat.id, kom_num + '\n' + kom_date + '\n' + kom_link)

        k4 = types.ReplyKeyboardMarkup(True, False)
        k4.row('Показать 10 следующих ответов', 'Ввести новый запрос')
        send = bbot.send_message(message.chat.id, "Готово, чего еще изволите", reply_markup=k4)
        bbot.register_next_step_handler(send, search2)
    except:
        bbot.send_message(message.chat.id, "Нет совпадений")
        send = bbot.send_message(message.chat.id, "ВВедите запрос")
        bbot.register_next_step_handler(send, ks)

def search2(message):
    if message.text == 'Показать 10 следующих ответов':
        bbot.register_next_step_handler(message, search)
    elif message.text == 'Ввести новый запрос':
        send = bbot.send_message(message.chat.id, "Введите новый запрос:")
        bbot.register_next_step_handler(send, ks)

bbot.polling(none_stop=True)
