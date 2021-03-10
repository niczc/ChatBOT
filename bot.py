import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Olá, operador(a) ' + update.message.from_user.first_name + "! \nTemos disponiveis os seguintes comandos:\n \\absorcao e \\exaustao"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def feedback(update, context):
    message = 'Por favor, deixe um feedback: '
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboad=True))
    return STATE1

def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = "Seu feedback foi muito curto, conte-nos mais por favor"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigado pelo feedback, lhe desejo uma semana repleta de gains!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def inputFeedback2(update, context):
    message = "Muito obrigado pelo feedback, lhe desejo uma semana repleta de gains!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def absorcao(update, context):
    message = "Se você está vendo que estão agredindo forte pra um lado, o volume cresce porém o preço não desloca existe uma grande possibilidade de estar acontecendo uma absorção!"    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def exaustao(update, context):
    message = "Mercado está perdendo força após um movimento forte e com um intervalo maior entre as agressões? Pode estar acontecendo uma exaustão, fique atento! "
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
 
def cancel(update, context):
    return ConversationHandler.END


def main():
    token = '1595466561:AAF2MtUACIttTpsZC_rURzsV5acLj2Jr4QE'
    updater = Updater(token=token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('absorcao', absorcao))
    updater.dispatcher.add_handler(CommandHandler('exaustao', exaustao))
    
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('feedback', feedback)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFeedback)],
            STATE2: [MessageHandler(Filters.text, inputFeedback2)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)
    
    
    updater.start_polling()
    print(str(updater))
    updater.idle()
    
    


if __name__ == '__main__':
    main()