#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import urllib.request
link = 'https://ulkabo.github.io/content-for-telegtam-bot/data/%D0%94%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%20%D0%BE%D1%81%D0%B2%D1%96%D1%82%D0%B0.txt'
        
import logging
from telegram import Update, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler,
                          ConversationHandler, CallbackContext )
import datetime
#file = open("users.txt", '+')
import sqlite3


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

contents = {'start' : {'text' :['data/start1.txt','data/start2.txt'],
                       'photo':[],
                       'next_menu': 
                          {'kafedra' : {'text' :['data/start_kafedra.txt'],
                                        'photo': [],
                                    'next_menu':{ 'vykladachi'  : {'text' : ['data/start_kafedra_vykladachi_with_url.txt'],
                                                                 'photo': []},
                                                'vidminnosti' : {'text' : ['data/start_kafedra_vidminnosti.txt'],
                                                                 'photo': []},
                                                'istoria'     : {'text' : ['data/sstart_kafedra_istoria.txt'],
                                                                 'photo': ['data/start_kafedra_istoria_urls_photo.txt']},
                                                'auditorii'   : {'text' : ['data/start_kafedra_auditorii.txt'],
                                                                 'photo': ['data/start_kafedra_auditorii_urls_photo.txt']},
                                                'vypusnyki'   : {'text' : ['data/start_kafedra_vypusnyki_with_url.txt'],
                                                                 'photo': []},
                                    }},
                       'mozhlyvosti' :{'text' : ['data/start_mozhlyvosti.txt'],
                                       'photo': [],
                                    'next_menu': {'proektnnavch'   : {'text': ['data/start_mozhlyvosti_proektnnavch_with_ulr.txt'],
                                                                    'photo':[]},
                                                'dualosvita'     : {'text': ['data/start_mozhlyvosti_dualoscita.txt'],
                                                                    'photo':[]},
                                                'pratsevlashuv'  : {'text': ['data/start_mozhlyvosti_pratsevlashtuv.txt'],
                                                                    'photo':[]},
                                                'praktika'       : {'text': ['data/start_mozhlyvosti_praktika.txt'],
                                                                    'photo':[]},
                                        }},
                       'umovy'    : {'text' : ['data/start_umovy.txt'],
                                       'photo': [],
                                    'next_menu': {'predmetiZNO'     : {'text': ['data/start_umovy_predmetiZNO.txt'],
                                                                    'photo':[]},
                                                'rozrakhunokBalu' : {'text': ['data/start_umovy_rozrakhunokBalu.txt'],
                                                                    'photo':[]},
                                                'etapy'           : {'text': ['data/start_umovy_etapy.txt'],
                                                                    'photo':[]},
                                                'posylannya'      : {'text': ['data/start_umovy_posylannya_with_url.txt'],
                                                                    'photo':[]},
                                                'kilkistMists'    : {'text': ['data/start_umovy_kilkistMists.txt'],
                                                                    'photo':[]},
                                      }}
                     }}
            }
def read_content(file):
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update : Update, context : CallbackContext):
    '''
    print(1)
    user = update.message.from_user
    file = open("users.txt", 'a+')
    n = user.first_name +' '
    print(2)
    n += user.last_name if user.last_name else ''
    name = n + ' ' + 'id: ' + str(user.id) + ' ' \
           + datetime.datetime.now().strftime("%Y %B %d. %A, %I: %M%p") \
           + ' ' + str(datetime.datetime.now())
    print(3)
    file.write(name + '\n')
    file.close()
    print(4)
    '''
    content = read_content(contents['start']['text'][0])
    keyboard = [
        [InlineKeyboardButton("Кафедра КМАД", callback_data = "kafedra")],
        [InlineKeyboardButton("Можливості для студентів", callback_data = "mozhlyvosti")],
        [InlineKeyboardButton("Умови вступу", callback_data = "umovy")]
        ]
    reply = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(content, parse_mode = "Markdown")
    url_photo = "http://web.kpi.kharkov.ua/kmmm/wp-content/uploads/sites/110/2013/09/Slide3.jpg"
    update.message.reply_photo(url_photo)
    
    #update.message.bot.send_photo(chat_id = update.message.from_user.id, photo = url_photo)
    update.message.reply_text("Обери, будь-ласка, теми, які тобі цікаві" , reply_markup = reply )
    

def kafedra (update : Update, context : CallbackContext):
    content = read_content(contents['start']['next_menu']['kafedra']['text'][0])
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Викладачі", callback_data = "vykladachi")],
        [InlineKeyboardButton("Відмінності кафедри", callback_data = "vidminnosti")],
        [InlineKeyboardButton("Історія кафедри", callback_data = "istoria")],
        [InlineKeyboardButton("Аудиторії кафедри", callback_data = "auditorii")],
        [InlineKeyboardButton("Наші випускники", callback_data = "vypusnyki")]
        ]
    reply = InlineKeyboardMarkup(keyboard)

    url_photo = "https://ulkabo.github.io/content-for-telegtam-bot/data/images/u1.jpg"

    query.message.bot.send_photo(chat_id = update.callback_query.message.chat.id, photo = url_photo)
    query.message.reply_text(text = content, reply_markup = reply)


def mozhlyvosti (update : Update, context : CallbackContext):
    
    content = read_content(contents['start']['next_menu']['mozhlyvosti']['text'][0])
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Проєктне навчання", callback_data = "proektnnavch")],
        [InlineKeyboardButton("Дуальна освіта", callback_data = "dualosvita")],
        [InlineKeyboardButton("Працевлаштування", callback_data = "pratsevlashuv")],
        [InlineKeyboardButton("Практика", callback_data = "praktika")],
        ]
    reply = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(text = content, reply_markup = reply)
        
def umovy (update : Update, context : CallbackContext):
    
    content = read_content(contents['start']['next_menu']['umovy']['text'][0])
    query = update.callback_query
    query.answer()
    keyboard = [
##        [InlineKeyboardButton("Конкурсні предмети ЗНО", callback_data = "predmetiZNO")],
        [InlineKeyboardButton("Розрахунок конкурсного балу", callback_data = "rozrakhunokBalu")],
        [InlineKeyboardButton("Етапи вступної кампанії", callback_data = "etapy")],
        [InlineKeyboardButton("Корисні посилання", callback_data = "posylannya")],
        [InlineKeyboardButton("Кількість бюджетних та контрактних місць для вступників", callback_data = "kilkistMists")],
        ]
    reply = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(text = content, reply_markup = reply)

def vykladachi (update : Update, context : CallbackContext):
    
    content = read_content(contents['start']['next_menu']['kafedra']['next_menu']['vykladachi']['text'][0])
    query = update.callback_query
    query.answer()
    
    query.message.reply_text(text = content, parse_mode = "Markdown")

def vidminnosti (update : Update, context : CallbackContext):
    
    content = read_content(contents['start']['next_menu']['kafedra']['next_menu']['vidminnosti']['text'][0])
    query = update.callback_query
    query.answer()
    
    query.message.reply_text(text = content, parse_mode = "Markdown")


    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Heeeeeelp!')

def end(update, context):
    global updater
    """Send a message when the command /help is issued."""
    update.message.reply_text('Bie!')
    updater.stop_polling()

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    
    """Start the bot."""
    
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1622026876:AAGSPO1cWixVtEb0Zw8PKJxNa-KfQUh7818", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("end", end))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(mozhlyvosti, pattern = "mozhlyvosti"))
    dp.add_handler(CallbackQueryHandler(umovy, pattern = "umovy"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(vykladachi, pattern = "vykladachi"))
    dp.add_handler(CallbackQueryHandler(vidminnosti, pattern = "vidminnosti"))
    '''dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = "kafedra"))
    '''
    
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
