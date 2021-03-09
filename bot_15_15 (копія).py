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

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    kb_start = [
            [InlineKeyboardButton("Кафедра КМАД", callback_data = "kafedra_KMAD")],
            [InlineKeyboardButton("Можливості для студентів", callback_data = "moglyv_stud")],
            [InlineKeyboardButton("Умови вступу", callback_data = "umovy_vstypy")],
    ]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text("Привіт! \
                    Цей чат-бот допоможе тобі познайомитися з ", reply_markup = reply)
    
    #update.message.reply_text("О кафедре /kafedra_KMAD ")
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def kafedra_KMAD(update, context):
    
    kb_kafedra =[
        
        [InlineKeyboardButton('Викладачі',callback_data = 'vikladachi')],
        [InlineKeyboardButton('Принципи навчання на кафедрі ',callback_data = 'principi')],
        [InlineKeyboardButton('Історія кафедри ',callback_data = 'istoriyaKafedry')],
        [InlineKeyboardButton('Аудиторії кафедри',callback_data = 'auditoryua')],
        [InlineKeyboardButton('Наші випускники',callback_data = 'vipuskniki')]
        ]
    
    reply1 = InlineKeyboardMarkup(kb_kafedra)
    update.callback_query.message.reply_text('З чого почнемо? ',reply_markup = reply1)
    url_photo = "https://picsum.photos/id/1084/536/354?grayscale"
    print(update.callback_query.message.chat.id )
    #update.callback_query.message.bot.send_photo(chat_id =update.callback_query.message.chat.id , photo = url_photo)
    #update.callback_query.message.bot.send_photo(chat_id = 763174940 , photo = url_photo)
    update.callback_query.message.reply_photo(url_photo)
def moglyv_stud(update, context):
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?  ')
    kb_moglyv_stud=[[InlineKeyboardButton("Проєктне навчання(в сториз“проєкти”)",callback_data = "")],
                             [InlineKeyboardButton("Дуальна освіта",callback_data = "")],
                             [InlineKeyboardButton("Працевлаштування",callback_data = "")]
                             [InlineKeyboardButton("Практика",callback_data = "")]
]
    reply2 = InlineKeyboardMarkup(kb_moglyv_stud)
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?  ',reply_markup = reply2)
def umovy_vstypy(update, context):
    update.callback_query.message.reply_text('Обери підпункт, який тобі цікавиий ')
    
def vikladachi(update, context):
    update.callback_query.message.reply_text('')
def principi(update, context):
    update.callback_query.message.reply_text('')
def istoriyaKafedry(update, context):
    update.callback_query.message.reply_text('')
def auditoryua(update, context):
    update.callback_query.message.reply_text('')
def vipuskniki(update, context):
    update.callback_query.message.reply_text('')
    
def main():

    updater = Updater("1622026876:AAGSPO1cWixVtEb0Zw8PKJxNa-KfQUh7818", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(kafedra_KMAD, pattern = 'kafedra_KMAD'))
    dp.add_handler(CallbackQueryHandler(moglyv_stud, pattern = 'moglyv_stud'))
    dp.add_handler(CallbackQueryHandler(umovy_vstypy, pattern = 'umovy_vstypy'))
    
    dp.add_handler(CallbackQueryHandler(vikladachi , pattern = "vikladachi"))
    dp.add_handler(CallbackQueryHandler(principi , pattern = "principi"))
    dp.add_handler(CallbackQueryHandler(istoriyaKafedry , pattern = "istoriyaKafedry"))
    dp.add_handler(CallbackQueryHandler(auditoryua , pattern = "auditoryua"))
    dp.add_handler(CallbackQueryHandler(vipuskniki , pattern = "vipuskniki"))

    dp.add_handler(MessageHandler(Filters.text, echo))


    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
