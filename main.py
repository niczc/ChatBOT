import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Olá, operador(a) ' + update.message.from_user.first_name + "! \nTemos disponiveis os seguintes comandos:\n\n /rules\n /absorcao\n /exaustao\n /youtube\n /replay\n /feedback\n"
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
  
def replay(update, context):
    message = "RAPEIZE... \n \n ## REPLAY n°1 \n \n 📌 Sexta-Feira, 12,  as 20h \n 📌 executor : Lucas \n ⚠️ Dia Replay : Será sorteado no dia do replay via sorteador \n ⚠️ Responsável pelo link : Lucas"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def youtube(update, context):
    message = "Link do canal do youtube: https://www.youtube.com/"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def vinhoAgora(update, context):
    message = "Primeiro vá estudar, tá pensando que é o Caique??"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def rules(update, context):
    message = "É desejável e necessário que todos os participantes estejam cientes e de acordo com:\n \n 📌 REGRAS DO CANAL \n \n ✅ PERMITIDO ✅  \n \n 📌 Dúvidas sobre os replays e seus convidados, dia, horário específico; \n \n 📌 Sugestões sobre os convidados para rodar o replay, no dia de replay: (Profissionais ou amadores que podemos contatar).\n \n 📌 NÃO HÁ distinção de habilidades, qualquer um pode ficar a vontade para pedir e realizar um replay caso queira, será incluído no CRONOGRAMA DE CONVIDADOS.\n \n ❌ NÃO É PERMITIDO ❌\n \n 📌 NÃO é um grupo para troca de informações de operações no dia-a-dia e nem durante o pregão;\n \n 📌 NÃO MANDEM RELATÓRIO DE PERFORMANCE; \n \n 📌 GRUPO EXCLUSIVO PARA TROCA DE EXPERIÊNCIAS E TIRA DÚVIDAS DE REPLAYS;\n \n______________________________\n \n 📌 Todos os estudos, dúvidas, troca de ideias, poderão ser feitas pós-replay e em qualquer dia e horário que tenha dúvida;\n \n 📌 TODOS OS REPLAYS SERÃO GRAVADOS, RENDERIZADOS E ENVIADOS O LINK AQUI PARA ACOMPANHAR POSTERIORMENTE;\n \n 📌 Ao fim de cada Replay teremos espaço para perguntas e questionamentos ao convidado que executou o Replay de mercado e narrou sua análise para os presentes na sala de reunião;\n (Via Zoom ou Google Meets)\n \n 📌 FRISANDO, o intuito deste canal é gerar conteúdo em Replay, estudo em replay, convidar profissionais, amadores e pessoas que estão firmes e ativos no estudo de Fluxo/Tape reading, específicamente no DÓLAR FUTURO.\n \n ______________________________\n \n ‼️‼️As regras é só uma maneira de manter um objetivo claro e único, que é estudo de replays de mercado e análise intraday e macro econômica ‼️‼️"
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
    updater.dispatcher.add_handler(CommandHandler('replay', replay))
    updater.dispatcher.add_handler(CommandHandler('youtube', youtube))
    updater.dispatcher.add_handler(CommandHandler('rules', rules))
    updater.dispatcher.add_handler(CommandHandler('vinhoAgora', vinhoAgora))

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
