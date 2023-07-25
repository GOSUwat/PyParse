import telebot 
import config
from parse import Parsing
from db import FindOptimal
from time import sleep
from threading import Thread


bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def get_url(message):
    
    if "https://www.avito.ru" in message.text:
        config.URL = message.text
        config.U_ID = message.from_user.id
        bot.send_message(config.U_ID,"Собирает не все обьявления, не удаляет старые. Присылает сообщение 1 раз в час.")
        prs = Parsing()
        prs.get_source()
        
    

def feedback():
    x = FindOptimal()
    prs = Parsing()
    for user in x.get_users:
        price,url,price_curr = x.find_min(user)
        send_message(user,url,price,price_curr)
        config.U_ID = user
        config.URL = str(x.get_sUrl(user))
        prs.get_source()
        sleep(20)


def send_message(user,url,price,price_curr):
    try:
        bot.send_message(int(user),f"Самое дешевое обьявление {url} по цене {price}{price_curr}")
    except Exception as e:
        print(e)
        sleep(40)
        



    
    
