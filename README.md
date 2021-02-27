# content-for-telegtam-bot
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
    #main
    dp.add_handler(CallbackQueryHandler(vikladachi , pattern = "vikladachi"))
    dp.add_handler(CallbackQueryHandler(principi , pattern = "principi"))
    dp.add_handler(CallbackQueryHandler(istoriyaKafedry , pattern = "istoriyaKafedry"))
    dp.add_handler(CallbackQueryHandler(auditoryua , pattern = "auditoryua"))
    dp.add_handler(CallbackQueryHandler(vipuskniki , pattern = "vipuskniki"))
