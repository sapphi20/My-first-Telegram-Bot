# -*- coding: utf-8 -*-
import json
import telepot
import time
from telepot.loop import MessageLoop
import urllib.request
from config import *

bot = telepot.Bot(bot_token)


# MessageLoop espera a que reciba un mensaje
# handle
def handle(msg):
    chat_id = msg['chat']['id']  # guarda id del chat del que se recibe el mensaje
    mensaje = msg['text']  # texto del mensaje
    # bot.sendMessage(chat_id, "que tal") #bot envia un mensaje al chat por el que recibe el mensaje
    a = mensaje.split(' ')  # separa el mensaje en 2
    comando = a[0]
    resto = a[1]  # el resto del mensaje
    if comando.startswith('/region'):
        bot.sendMessage(chat_id, token_price(resto))

#Entrega el precio del token en la region indicada
def token_price(region):
    lonk = "https://data.wowtoken.info/wowtoken.json"
    with urllib.request.urlopen(lonk) as url:
        data = json.loads(url.read())
        return data['update'][region]['raw']['buy']


MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)