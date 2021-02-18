#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
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

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update : Update, context : CallbackContext):
    user = update.message.from_user
    print('-----',user)
    print('---____--',user.username)
    print('----_______   -',user.id)
    print('-________-------     ---',datetime.datetime.now().strftime("%Y %B %d. %A, %I: %M%p") )
    file = open("users.txt", 'a+')
    n = user.first_name +' '
    n += user.last_name if user.last_name else ''
    print(n)
    name = n + ' ' + 'id: ' + str(user.id) + ' ' + datetime.datetime.now().strftime("%Y %B %d. %A, %I: %M%p") + ' ' + str(datetime.datetime.now())
    print(name)
    file.write(name + '\n')
    
    #print(user.first_name, user.last_name)
    file.close()
    """Send a message when the command /start is issued."""

    content = "Привіт! \n\
                Цей чат-бот допоможе тобі познайомитися з кафедрою ближче.\
                Ти дізнаєшся про викладачів, спеціальності, додаткові можливості для студентів та умови вступу. \
                Натискай /start "
    
    url_photo = 'https://picsum.photos/id/237/200/300'
    keyboard = [
        [InlineKeyboardButton("Викладачі", callback_data = "m11_викладачі")],
        [InlineKeyboardButton("Про кафедру", callback_data = "m12_кафедра")],
        [InlineKeyboardButton("для студентів", callback_data = "m13_студенти")]
        ]
    reply = InlineKeyboardMarkup(keyboard)
    #update.message.reply_text(dir(update.message.bot))
    update.message.reply_text(content)
    
    url_photo = "http://web.kpi.kharkov.ua/kmmm/wp-content/uploads/sites/110/2013/09/Slide3.jpg"
    update.message.bot.send_photo(chat_id = update.message.from_user.id, photo = url_photo)
    update.message.reply_text("Обери, будь-ласка, теми, які тобі цікаві" , reply_markup = reply )
    return 'step1'
    
def menu11 (update : Update, context : CallbackContext):

    content = "На кафедрі працює 26 викладачів, у тому числі 4 професорів, \
                                доктори наук, 16 доцентів, кандидати наук."
    query = update.callback_query
    query.answer()
    wU = urllib.request.urlopen(link)
    a = wU.read()
    b = a.decode(encoding = 'utf-8')
    print(a)
    print(b)
    content = b
    kb = [['/start','/end']]
    reply_kb_markup = ReplyKeyboardMarkup(kb, resize_keyboard = True,
                                          one_time_keyboard = False)
    keyboard = [
        [InlineKeyboardButton("Викладачі", callback_data = "m111_викладачі")],
        [InlineKeyboardButton("Професори", callback_data = "m112_професора")],
        [InlineKeyboardButton("доктори наук", callback_data = "m113_доктора")]
        ]
    reply = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(text = 'внизу кнопки', reply_markup =  reply_kb_markup)
    #update.message.reply_text(text = 'внизу кнопки', reply_markup =  reply_kb_markup)
    #print(dir(query), dir(query.message))
    query.message.reply_text(text = content, reply_markup = reply)
    #query.edit_message_text(text = content, reply_markup = reply)
    #update.message.reply_text(content, reply_markup = reply )
    return 'step2'

def menu12 (update : Update, context : CallbackContext):
    content = "На кафедрі КМАД реалізується пілотний проект по розробці, \
                                апробації та реалізації інноваційної освітньої системи на \
                                основі технологій проектного навчання (project based learning), \
                                навчання за запитами (inquire learning), пірингового навчання P2P \
                                (peer-to-peer) і геймифікації освітнього процесу в рамках Всесвітньої \
                                ініціативи реформування інженерної освіти CDIO Iinitiative \
                                http://www.cdio.org/about. Проект реалізується за підтримки фонду \
                                Василя Хмельницького K-Fund http://kfund.ua/. \
                            Кафедра КМАД увійшла до складу ініціативної групи по створенню \
                            Української асоціації датистики (UkrainianAssociationonDataScience), \
                               серед завдань якої важливе місце займає створення Української \
                               освітньої програми в галузі науки про даних (“DataScience”) – один з \
                               найбільш сучасних напрямів комп’ютерних наук. Програма розробляється на \
                               основі і за підтримки Європейського проекту EDISON http://edison-project.eu, \
                               спрямованого на створення професії DataScientist для європейської\
                               промисловості та прикладних досліджень."
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Історія кафедри", callback_data = "m121_історія")],
        [InlineKeyboardButton("Аудиторії кафедри", callback_data = "m122_аудиторії")],
        [InlineKeyboardButton("Наші випускники", callback_data = "m123_випускники")]
        ]
    reply = InlineKeyboardMarkup(keyboard)
    #url_photo = "https://i.picsum.photos/id/0/5616/3744.jpg?hmac=3GAAioiQziMGEtLbfrdbcoenXoWAW-zlyEAMkfEdBzQ"
    url_photo = "https://ulkabo.github.io/content-for-telegtam-bot/data/images/u1.jpg"
    query.message.reply_text(text = content)
    #print(update)
    query.message.bot.send_photo(chat_id = update.callback_query.message.chat.id, photo = url_photo)
    query.message.reply_text(text = 'Що тобі ще цікаво ?', reply_markup = reply)
    #query.edit_message_text(text = content, reply_markup = reply)
    #update.message.reply_text(content, reply_markup = reply )
    return 'step2'

def menu13 (update : Update, context : CallbackContext):
    print(1)
    file = open("data/Дуальна освіта.txt", 'r')
    print(2)
    content = file.read()
    file.close()
    query = update.callback_query
    query.answer()
    keyboard = [
        [InlineKeyboardButton("Викладачі", callback_data = "m111_викладачі")],
        [InlineKeyboardButton("Професори", callback_data = "m112_професора")],
        [InlineKeyboardButton("доктори наук", callback_data = "m113_доктора")]
        ]
    reply = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(text = content, reply_markup = reply)
    #query.edit_message_text(text = content, reply_markup = reply)
    #update.message.reply_text(content, reply_markup = reply )
    return 'step2'
        
def menu111 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu112 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu113 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu121 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu122 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu123 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu131 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu132 (update : Update, context : CallbackContext):
    pass
    return 'step3'
def menu133 (update : Update, context : CallbackContext):
    pass
    return 'step3'
    
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
    dp.add_handler(CommandHandler("end", end))
    dp.add_handler(CommandHandler("help", help))

    # new one
    
    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            'step1' : [
                      CallbackQueryHandler(menu11, pattern = "m11_викладачі"),
                      CallbackQueryHandler(menu12, pattern = "m12_кафедра"),
                      CallbackQueryHandler(menu13, pattern = "m13_студенти"),
                       ],
            'step2' : [
                      CallbackQueryHandler(menu111, pattern = "m111_викладачі"),
                      CallbackQueryHandler(menu112, pattern = "m112_професора"),
                      CallbackQueryHandler(menu113, pattern = "m113_доктора"),
                       ],
            'step2' : [
                      CallbackQueryHandler(menu121, pattern = "m121_історія"),
                      CallbackQueryHandler(menu122, pattern = "m122_аудиторії"),
                      CallbackQueryHandler(menu123, pattern = "m123_випускники"),
                       ],
            'step2' : [
                      CallbackQueryHandler(menu131, pattern = "m131_Проєктне навчання"),
                      CallbackQueryHandler(menu132, pattern = "m132_Практика"),
                      CallbackQueryHandler(menu133, pattern = "m133_Працевлаштування"),
                       ],

                 },
        fallbacks = [CommandHandler('start', start)],
        )
    dp.add_handler(conv_handler)
    
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
