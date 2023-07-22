import telebot 
from db import DB
from parse import get_source

bot = telebot.TeleBot('')

nick_name = ""
parse_link = ""

@bot.message_handler(content_types=['text'])


def start(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    if "https://www.avito.ru" in message.text:
        db = DB()
        URL = message.text
        #get_source(url = URL)
        get_source(message.from_user.id,URL)
        #db.db_connect(message.from_user.id,URL,href,data)
    #bot.send_message(message.from_user.id, f"{message.from_user.id}", reply_markup=markup)
    
    
    
        
bot.polling(none_stop=True, interval=0)