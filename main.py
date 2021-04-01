import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Olá, operador(a) ' + update.message.from_user.first_name + "! \nTemos disponiveis os seguintes comandos:\n \n ⚠️ OPERACIONAIS ⚠️ \n /absorcao\n /exaustao\n /lote_liquidez\n /escora\n \n ⚠️ FERRAMENTAS ⚠️ \n /book\n /times_e_trades\n /vwap\n /ajuste\n \n ⚠️ INFORMAÇÕES ⚠️ \n /rules\n /youtube\n /replay\n /ordem_dos_replays\n /vinhoAgora\n"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def lista_replay(update, context):
    message = '⚠️  Ordem Semanal dos Replays:  ⚠️\n 📌 Quinta-Feira 19:00 (01/04):Guilherme Turibio e Wender Junior \n 📌Sábado 13:00 (03/04): Guilherme Turibio e Bruno Pondan'
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def replay(update, context):
    message = "RAPEIZE... \n \n ## REPLAY n°14 \n \n 📌 Quinta-Feira, 01,  as 19hrs \n 📌 executores :Guilherme Turibio e Wender Junior \n ⚠️ Dia Replay: Será sorteado no dia do replay via sorteador "
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def feedback(update, context):
    message = 'Por favor, deixe um feedback: '
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboad=True))
    return STATE1

def inputFeedback(update, context):
    feedback = update.message.text
    print(feedback)
    if len(feedback) < 10:
        message = "Seu feedback foi muito curto, conte-nos mais sobre sua experiência"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    else:
        message = "Muito obrigado pelo feedback, lhe desejo uma semana repleta de gains!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def inputFeedback2(update, context):
    message = "Muito obrigado pelo feedback, lhe desejo uma semana repleta de gains!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
  


def youtube(update, context):
    message = "Link do canal do youtube:\n https://www.youtube.com/channel/UCqj3NoSb5o_9vcg8QRAC2Hw"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# def resultado(update, context):
#  função dos id usuario
#  recupera a função adicionando um randon + a mensagem a ser acrescentada ao usuario
#  retorna na tela o resultado

def vinhoAgora(update, context):
    message = "Você tem que estudar primeiro seu Rubinho, tá pensando que é o Caique??"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def rules(update, context):
    message = "É desejável e necessário que todos os participantes estejam cientes e de acordo com:\n \n 📌 REGRAS DO CANAL \n \n ✅ PERMITIDO ✅  \n \n 📌 Dúvidas sobre os replays e seus convidados, dia, horário específico; \n \n 📌 Sugestões sobre os convidados para rodar o replay, no dia de replay: (Profissionais ou amadores que podemos contatar).\n \n 📌 NÃO HÁ distinção de habilidades, qualquer um pode ficar a vontade para pedir e realizar um replay caso queira, será incluído no CRONOGRAMA DE CONVIDADOS.\n \n ❌ NÃO É PERMITIDO ❌\n \n 📌 NÃO é um grupo para troca de informações de operações no dia-a-dia e nem durante o pregão;\n \n 📌 NÃO MANDEM RELATÓRIO DE PERFORMANCE; \n \n 📌 GRUPO EXCLUSIVO PARA TROCA DE EXPERIÊNCIAS E TIRA DÚVIDAS DE REPLAYS;\n \n______________________________\n \n 📌 Todos os estudos, dúvidas, troca de ideias, poderão ser feitas pós-replay e em qualquer dia e horário que tenha dúvida;\n \n 📌 TODOS OS REPLAYS SERÃO GRAVADOS, RENDERIZADOS E ENVIADOS O LINK AQUI PARA ACOMPANHAR POSTERIORMENTE;\n \n 📌 Ao fim de cada Replay teremos espaço para perguntas e questionamentos ao convidado que executou o Replay de mercado e narrou sua análise para os presentes na sala de reunião;\n (Via Zoom ou Google Meets)\n \n 📌 FRISANDO, o intuito deste canal é gerar conteúdo em Replay, estudo em replay, convidar profissionais, amadores e pessoas que estão firmes e ativos no estudo de Fluxo/Tape reading, específicamente no DÓLAR FUTURO.\n \n ______________________________\n \n ‼️‼️As regras é só uma maneira de manter um objetivo claro e único, que é estudo de replays de mercado e análise intraday e macro econômica ‼️‼️"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def absorcao(update, context):
    message = "Se você está vendo que estão agredindo forte pra um lado, o volume cresce porém o preço não desloca existe uma grande possibilidade de estar acontecendo uma absorção!"    
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def exaustao(update, context):
    message = "Mercado está perdendo força após um movimento forte de alta ou baixa, com um intervalo maior entre as agressões, existindo lotes para buscar mas não possui força para continuar? Pode estar acontecendo uma exaustão, fique atento! "
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def liquidez(update, context):
    message = "Muitas vezes confundido com os lotes de escora, lotes de liquidez ocorrem quando um player comprado/vendido está colocando lotes na contraparte do book chamando o mercado pro lado que seja a favor de sua posição e assim aumente o seu lucro."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
def escora(update, context):
    message = "Voce percebe que um player está comprado/vendido e continua deixando lote no book de ofertas a favor de sua posição? Ele pode estar querendo defender aquele nível de preço. Lotes de escora são lotes para defender uma região."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    

def book(update, context):
    message = "Por ele é possível enxergar as intenções de compra e venda que o ativo está sendo negociado."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def times(update, context):
    message = "Com essa ferramente você conseguirar visualizar todos os negocios que foram efetuados. Nele é informado o comprador, vendedor, o horário e a quantidade negociada."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def vwap(update, context):
    message = "A VWAP ou Preço Médio Ponderado Por Volume é um dos indicador técnicos mais famosos do mercado. Por ele marcar uma região de muito volume financeiro, é comum institucionais estarem posicionados na região e dessa forma demonstrar interesse em protege-la. "
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def ajuste(update, context):
     message = "Está pensando em ficar posicionado até o próximo pregão? Então é melhor ficar atento ao ajuste, pois é no preço do ajuste que você ficará posicionado. Ele é um ajuste financeiro, podendo ser débito ou crédito, no próximo dia útil na conta dos investidores. "
     context.bot.send_message(chat_id=update.effective_chat.id, text=message)
      
def cancel(update, context):
    return ConversationHandler.END


def main():
    token = '1595466561:AAF2MtUACIttTpsZC_rURzsV5acLj2Jr4QE'
    updater = Updater(token=token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(CommandHandler('absorcao', absorcao))
    updater.dispatcher.add_handler(CommandHandler('exaustao', exaustao))
    updater.dispatcher.add_handler(CommandHandler('book', book))
    updater.dispatcher.add_handler(CommandHandler('times_e_trades', times))
    updater.dispatcher.add_handler(CommandHandler('vwap', vwap))
    updater.dispatcher.add_handler(CommandHandler('replay', replay))
    updater.dispatcher.add_handler(CommandHandler('youtube', youtube))
    updater.dispatcher.add_handler(CommandHandler('rules', rules))
    updater.dispatcher.add_handler(CommandHandler('vinhoAgora', vinhoAgora))
    updater.dispatcher.add_handler(CommandHandler('ordem_dos_replays', lista_replay))
    updater.dispatcher.add_handler(CommandHandler('ajuste', ajuste))
    updater.dispatcher.add_handler(CommandHandler('escora', escora))
    updater.dispatcher.add_handler(CommandHandler('lote_liquidez', liquidez))

    
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
