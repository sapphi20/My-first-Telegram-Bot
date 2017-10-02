# -*- coding: utf-8 -*-
import telepot
import time
from telepot.loop import MessageLoop

bot_token = '406091045:AAE-02I5NEO6INPjbyYqXB4fZjASaIX5Evo'
bot = telepot.Bot(bot_token)


# MessageLoop espera a que reciba un mensaje
# handle
def handle(msg):
    chat_id = msg['chat']['id']  # guarda id del chat del que se recibe el mensaje
    mensaje = msg['text']  # texto del mensaje
    # bot.sendMessage(chat_id, "que tal") #bot envia un mensaje al chat por el que recibe el mensaje
    a = mensaje.split(' ', 1)  # separa el mensaje en 2
    comando = a[0]
    resto = a[1]  # el resto del mensaje
    if comando.startswith('/echo'):
        bot.sendMessage(chat_id, resto)


MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)
