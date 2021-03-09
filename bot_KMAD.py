#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
import urllib.request
import logging
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler,
                          ConversationHandler, CallbackContext)
from telegram import Update, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import datetime
TOKEN = '1622026876:AAGSPO1cWixVtEb0Zw8PKJxNa-KfQUh7818'

link = 'https://ulkabo.github.io/content-for-telegtam-bot/data/'

#file = open("users.txt", '+')
#import sqlite3


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

contents = {'start': {'text': ['start1.txt', 'start2.txt'],
                      'photo': [],
                      'next_menu':
                      {'kafedra': {'text': ['start_kafedra.txt'],
                                   'photo': [],
                                   'next_menu': {'vykladachi': {'text': ['start_kafedra_vykladachi_with_url.txt'],
                                                                'photo': []},
                                                 'vidminnosti': {'text': ['start_kafedra_vidminnosti.txt'],
                                                                 'photo': []},
                                                 'istoria': {'text': ['start_kafedra_istoria.txt'],
                                                             'photo': ['start_kafedra_istoria_urls_photo.txt']},
                                                 'auditorii': {'text': ['start_kafedra_auditorii.txt'],
                                                               'photo': ['start_kafedra_auditorii_urls_photo.txt']},
                                                 'vypusnyki': {'text': ['start_kafedra_vypusnyki_with_url.txt'],
                                                               'photo': ['start_kafedra_vypusnyki_urls_photo.txt']},
                                                 }},
                       'mozhlyvosti': {'text': ['start_mozhlyvosti.txt'],
                                       'photo': [],
                                       'next_menu': {'proektnnavch': {'text': ['start_mozhlyvosti_proektnnavch_with_ulr.txt'],
                                                                      'photo': []},
                                                     'dualosvita': {'text': ['start_mozhlyvosti_dualoscita.txt'],
                                                                    'photo': []},
                                                     'pratsevlashuv': {'text': ['start_mozhlyvosti_pratsevlashtuv.txt'],
                                                                       'photo': []},
                                                     'praktika': {'text': ['start_mozhlyvosti_praktika.txt'],
                                                                  'photo': []},
                                                     }},
                       'umovy': {'text': ['start_umovy.txt'],
                                 'photo': [],
                                 'next_menu': {'predmetiZNO': {'text': ['start_umovy_predmetiZNO.txt'],
                                                               'photo': []},
                                               'rozrakhunokBalu': {'text': ['start_umovy_rozrakhunokBalu.txt'],
                                                                   'photo': []},
                                               'etapy': {'text': ['start_umovy_etapy.txt'],
                                                         'photo': []},
                                               'posylannya': {'text': ['start_umovy_posylannya_with_url.txt'],
                                                              'photo': []},
                                               'kilkistMists': {'text': ['start_umovy_kilkistMists.txt'],
                                                                'photo': []},
                                               }}
                       }}
            }
'''
keyboard_start = [[KeyboardButton("Кафедра КМАД"),
                   KeyboardButton("Можливості для студентів"),
                   KeyboardButton("Умови вступу")]]
'''
keyboard_start = [[KeyboardButton("НА ПОЧАТОК")]]
reply_kb_markup = ReplyKeyboardMarkup(keyboard_start, resize_keyboard=True,
                                      one_time_keyboard=False)

keyboard_kafedra = [
    [InlineKeyboardButton("Викладачі", callback_data="vykladachi")],
    [InlineKeyboardButton("Відмінності кафедри",
                          callback_data="vidminnosti")],
    [InlineKeyboardButton("Історія кафедри", callback_data="istoria")],
    [InlineKeyboardButton("Аудиторії кафедри", callback_data="auditorii")],
    [InlineKeyboardButton("Наші випускники", callback_data="vypusnyki")]
]
keyboard_mozhlyvosti = [
    [InlineKeyboardButton("Проєктне навчання",
                          callback_data="proektnnavch")],
    [InlineKeyboardButton("Дуальна освіта", callback_data="dualosvita")],
    [InlineKeyboardButton("Працевлаштування",
                          callback_data="pratsevlashuv")],
    [InlineKeyboardButton("Практика", callback_data="praktika")],
]
keyboard_umovy = [
    [InlineKeyboardButton("Конкурсні предмети ЗНО",
                          callback_data="predmetiZNO")],
    [InlineKeyboardButton("Розрахунок конкурсного балу",
                          callback_data="rozrakhunokBalu")],
    [InlineKeyboardButton("Етапи вступної кампанії",
                          callback_data="etapy")],
    [InlineKeyboardButton("Корисні посилання",
                          callback_data="posylannya")],
    [InlineKeyboardButton(
        "Кількість бюджетних та \nконтрактних місць для вступників", callback_data="kilkistMists")],
]
keyboard_backto_kafedra = [
    [InlineKeyboardButton("Назад",
                          callback_data="kafedra")]]
keyboard_backto_mozhlyvosti = [
    [InlineKeyboardButton("Назад",
                          callback_data="mozhlyvosti")]]
keyboard_backto_umovy = [
    [InlineKeyboardButton("Назад",
                          callback_data="umovy")]]


def read_content(url_file):
    #f = open(file, 'r')
    #text = f.read()
    # f.close()
    wU = urllib.request.urlopen(url_file)
    text = wU.read().decode(encoding='utf-8')

    return text


def start(update: Update, context: CallbackContext):
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
    print(link + contents['start']['text'][0])
    content = read_content(link + contents['start']['text'][0])
    print(content)
    keyboard = [
        [InlineKeyboardButton("Кафедра КМАД", callback_data="kafedra")],
        [InlineKeyboardButton("Можливості для студентів",
                              callback_data="mozhlyvosti")],
        [InlineKeyboardButton("Умови вступу", callback_data="umovy")]
    ]
    reply = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        content, reply_markup=reply_kb_markup, parse_mode="Markdown")
    url_photo = "http://web.kpi.kharkov.ua/kmmm/wp-content/uploads/sites/110/2013/09/Slide3.jpg"
    update.message.reply_photo(url_photo)
    content = read_content(link + contents['start']['text'][1])
    update.message.reply_text(content, reply_markup=reply)


'''
def kafedra_m(update: Update, context: CallbackContext):
    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['text'][0])
    reply = InlineKeyboardMarkup(keyboard_kafedra)
    update.message.reply_text(text=content, reply_markup=reply)


def mozhlyvosti_m(update: Update, context: CallbackContext):
    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['text'][0])
    reply = InlineKeyboardMarkup(keyboard_mozhlyvosti)
    update.message.reply_text(text=content, reply_markup=reply)


def umovy_m(update: Update, context: CallbackContext):
    content = read_content(
        link + contents['start']['next_menu']['umovy']['text'][0])
    reply = InlineKeyboardMarkup(keyboard_umovy)
    update.message.reply_text(text=content, reply_markup=reply)
'''


def kafedra(update: Update, context: CallbackContext):
    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_kafedra)
    query.message.reply_text(text=content, reply_markup=reply)


def mozhlyvosti(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_mozhlyvosti)
    query.message.reply_text(text=content, reply_markup=reply)


def umovy(update: Update, context: CallbackContext):

    content = read_content(
        link + contents['start']['next_menu']['umovy']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_umovy)
    query.message.reply_text(text=content, reply_markup=reply)


# -------------------------------**  block kafedra  **----------------------------

def vykladachi(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['next_menu']['vykladachi']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_kafedra)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")


def vidminnosti(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['next_menu']['vidminnosti']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_kafedra)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")


def istoria(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['next_menu']['istoria']['text'][0])
    content_lines = content.split('\n')
    photos = read_content(link +
                          contents['start']['next_menu']['kafedra']['next_menu']['istoria']['photo'][0])
    print(photos)
    photos = photos.split('\n')
    print(photos)
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_kafedra)
    step = len(content_lines) // len(photos)
    print(len(content_lines), len(photos), step)

    for i in range(len(photos)):
        print('b', i)
        query.message.reply_text(text='\n'.join(
            content_lines[i*step:(i+1)*step]), parse_mode="Markdown")
        print('m', i//step)
        query.message.reply_photo(link + photos[i])
        print('e', i)
        print('\n'.join(content_lines[i*step:]))
    query.message.reply_text(
        text='\n'.join(content_lines[i*step:]), reply_markup=reply, parse_mode="Markdown")


def auditorii(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['next_menu']['auditorii']['text'][0])
    content_lines = content.split('\n')
    photos = read_content(link +
                          contents['start']['next_menu']['kafedra']['next_menu']['auditorii']['photo'][0])
    photos = photos.split('\n')
    query = update.callback_query
    query.answer()
    reply = InlineKeyboardMarkup(keyboard_backto_kafedra)
    query.message.reply_text(text='\n'.join(
        content_lines[0:1]), parse_mode="Markdown")
    query.message.reply_photo(link + photos[0])
    query.message.reply_text(text='\n'.join(
        content_lines[2:7]), parse_mode="Markdown")
    query.message.reply_photo(link + photos[1])
    query.message.reply_photo(link + photos[2])
    query.message.reply_text(text='\n'.join(
        content_lines[7:8]), parse_mode="Markdown")
    query.message.reply_photo(link + photos[3])
    query.message.reply_text(
        text='\n'.join(content_lines[8:]), reply_markup=reply, parse_mode="Markdown")


def vypusnyki(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['kafedra']['next_menu']['vypusnyki']['text'][0])
    content_lines = content.split('\n')
    photos = read_content(link +
                          contents['start']['next_menu']['kafedra']['next_menu']['vypusnyki']['photo'][0])
    photos = photos.split('\n')
    query = update.callback_query
    query.answer()
    reply = InlineKeyboardMarkup(keyboard_backto_kafedra)
    print(reply)
    query.message.reply_text(text='\n'.join(
        content_lines[:13]), parse_mode="Markdown")
    query.message.reply_photo(link + photos[0])
    query.message.reply_text(
        text='\n'.join(content_lines[13:]), reply_markup=reply, parse_mode="Markdown")
# -------------------------------**  end block kafedra  **----------------------------


# -------------------------------**   block mozhlyvosti  **----------------------------

def proektnnavch(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['next_menu']['proektnnavch']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_mozhlyvosti)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")
    #query.message.reply_text(text="Що ще Вас цікавить ? ", reply_markup=reply)


def dualosvita(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['next_menu']['dualosvita']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_mozhlyvosti)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")
    #query.message.reply_text(text="Що ще Вас цікавить ? ", reply_markup=reply)


def pratsevlashuv(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['next_menu']['pratsevlashuv']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_mozhlyvosti)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")
    #query.message.reply_text(text="Що ще Вас цікавить ? ", reply_markup=reply)


def praktika(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['mozhlyvosti']['next_menu']['praktika']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_mozhlyvosti)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")
    #query.message.reply_text(text="Що ще Вас цікавить ? ", reply_markup=reply)
# -------------------------------**   end block mozhlyvosti  **----------------------------


# -------------------------------**   block umovy  **----------------------------

def predmetiZNO(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['umovy']['next_menu']['predmetiZNO']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_umovy)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")


def rozrakhunokBalu(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['umovy']['next_menu']['rozrakhunokBalu']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_umovy)
    query.message.reply_text(
        text=content, reply_markup=reply)  # , parse_mode="Markdown")


def etapy(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['umovy']['next_menu']['etapy']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_umovy)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")


def posylannya(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['umovy']['next_menu']['posylannya']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_umovy)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")


def kilkistMists(update: Update, context: CallbackContext):

    content = read_content(link +
                           contents['start']['next_menu']['umovy']['next_menu']['kilkistMists']['text'][0])
    query = update.callback_query
    query.answer()

    reply = InlineKeyboardMarkup(keyboard_backto_umovy)
    query.message.reply_text(
        text=content, reply_markup=reply, parse_mode="Markdown")

# -------------------------------**   end block umovy  **----------------------------


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    '''
    #"Кафедра КМАД", "Можливості для студентів", "Умови вступу"
    dp.add_handler(MessageHandler(Filters.regex('^Кафедра КМАД$'), kafedra_m))
    dp.add_handler(MessageHandler(Filters.regex(
        '^Можливості для студентів$'), mozhlyvosti_m))
    dp.add_handler(MessageHandler(Filters.regex('^Умови вступу$'), umovy_m))
    '''
    dp.add_handler(MessageHandler(Filters.regex('^НА ПОЧАТОК$'), start))

    dp.add_handler(CallbackQueryHandler(kafedra, pattern="kafedra"))
    dp.add_handler(CallbackQueryHandler(mozhlyvosti, pattern="mozhlyvosti"))
    dp.add_handler(CallbackQueryHandler(umovy, pattern="umovy"))

    dp.add_handler(CallbackQueryHandler(vykladachi, pattern="vykladachi"))
    dp.add_handler(CallbackQueryHandler(vidminnosti, pattern="vidminnosti"))
    dp.add_handler(CallbackQueryHandler(istoria, pattern="istoria"))
    dp.add_handler(CallbackQueryHandler(auditorii, pattern="auditorii"))
    dp.add_handler(CallbackQueryHandler(vypusnyki, pattern="vypusnyki"))

    dp.add_handler(CallbackQueryHandler(proektnnavch, pattern="proektnnavch"))
    dp.add_handler(CallbackQueryHandler(dualosvita, pattern="dualosvita"))
    dp.add_handler(CallbackQueryHandler(
        pratsevlashuv, pattern="pratsevlashuv"))
    dp.add_handler(CallbackQueryHandler(praktika, pattern="praktika"))

    dp.add_handler(CallbackQueryHandler(predmetiZNO, pattern="predmetiZNO"))
    dp.add_handler(CallbackQueryHandler(
        rozrakhunokBalu, pattern="rozrakhunokBalu"))
    dp.add_handler(CallbackQueryHandler(etapy, pattern="etapy"))
    dp.add_handler(CallbackQueryHandler(posylannya, pattern="posylannya"))
    dp.add_handler(CallbackQueryHandler(kilkistMists, pattern="kilkistMists"))

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
