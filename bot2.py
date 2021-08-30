import telebot
from telebot import types
from telebot import util, types
import time
import teoric
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_menu(message):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Operacionais", callback_data = "operacionais")
    item2 = types.InlineKeyboardButton("Ferramentas", callback_data = "ferramentas")
    item3 = types.InlineKeyboardButton('Psicologia do Trader', callback_data= 'psicologia')
    item4 = types.InlineKeyboardButton('Informações', callback_data= 'informacoes')
    mkup.add(item1, item2, item3, item4)
    text = "Olá, " + message.from_user.first_name +  " ,eu sou o Doleta. Precisa de ajuda? "
    bot.send_message(message.chat.id, text, reply_markup=mkup)

@bot.callback_query_handler(func = lambda call: call.data == 'operacionais')
def opera_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Absorção", callback_data = 'abs')
    item2 = types.InlineKeyboardButton("Exaustao", callback_data = 'ext')
    item3 = types.InlineKeyboardButton("Lote de Liquidez", callback_data = 'liq')
    item4 = types.InlineKeyboardButton("Lote de Escora", callback_data = 'esc')
    item5 = types.InlineKeyboardButton("Renovação", callback_data = 'ren')
    item6 = types.InlineKeyboardButton("Cancelamento", callback_data = 'can')
    item7 = types.InlineKeyboardButton("Back", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Operacionais"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)
    
@bot.callback_query_handler(func = lambda call: call.data == 'ferramentas')
def ferra_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Times & Trades", callback_data = 'time')
    item2 = types.InlineKeyboardButton("Book de Ofertas", callback_data = 'book')
    item3 = types.InlineKeyboardButton("Super DOM", callback_data = 'dom')
    item4 = types.InlineKeyboardButton("Volume At Price", callback_data = 'vol')
    item5 = types.InlineKeyboardButton("VWAP", callback_data = 'vwap')
    item6 = types.InlineKeyboardButton("Ajuste", callback_data = 'ajuste')
    item7 = types.InlineKeyboardButton("Back", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Ferramentas"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func = lambda call: call.data == 'psicologia')
def psico_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Ansiedade", callback_data = 'ansiedade')
    item2 = types.InlineKeyboardButton("Medo", callback_data = 'medo')
    item3 = types.InlineKeyboardButton("Não aceita os erros", callback_data = 'n_erros')
    item4 = types.InlineKeyboardButton("Auto Sabotagem", callback_data = 'sabotagem')
    item5 = types.InlineKeyboardButton("Não sabe perder", callback_data = 'n_perder')
    item6 = types.InlineKeyboardButton("Não sabe ganhar", callback_data = 'n_ganhar')
    item7 = types.InlineKeyboardButton("Pressa em ganhar dinheiro", callback_data = 'p_dinheiro')
    item8 = types.InlineKeyboardButton("Não ter paciencia pra estudar", callback_data = 'n_estudar')
    item9 = types.InlineKeyboardButton("Não saber traçar metas e objetivos", callback_data = 'n_metas')
    item10 = types.InlineKeyboardButton("Insegurança", callback_data = 'p_dinheiro')
    item11 = types.InlineKeyboardButton("Back", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7,item8, item9, item10, item11)
    text = "Psicologia do Trader por @RenanReligare"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func = lambda call: call.data == 'informacoes')
def opera_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Regras do Grupo", callback_data = 'abs')
    item2 = types.InlineKeyboardButton("Canal do Youtube", url = 'https://youtube.com.br/olhonoreplay')
    item3 = types.InlineKeyboardButton("Perfil do Instagram", url = 'https://instagram.com/olhonoreplay')
    item3 = types.InlineKeyboardButton("Replay do Dia", callback_data = 'replay')
    item4 = types.InlineKeyboardButton("Lista dos Replays", callback_data = 'lista')
    item5 = types.InlineKeyboardButton("Quero Vinho", callback_data = 'vinho')
    item6 = types.InlineKeyboardButton("Fale com o Desenvolvedor", url = 'https://t.me/Nicolasleao')
    item7 = types.InlineKeyboardButton("Back", callback_data = "back")
    mkup.add(item1, item2, item3, item4, item5, item6, item7)
    text = "Informações do Grupo"
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=mkup)


@bot.callback_query_handler(func = lambda call: call.data == 'back')
def bac_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Operacionais", callback_data = "operacionais")
    item2 = types.InlineKeyboardButton("Ferramentas", callback_data = "ferramentas")
    item3 = types.InlineKeyboardButton('Psicologia do Trader', callback_data= 'psicologia')
    item4 = types.InlineKeyboardButton('Informações', callback_data= 'informacoes')
    mkup.add(item1, item2, item3, item4)
    text = "Você novamente por aqui? Surgiu mais alguma dúvida? "
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)   


@bot.callback_query_handler(func = lambda call: True)
def asnwer(call):
    #operacionais
    if call.data == 'abs':
        bot.send_message(call.message.chat.id, teoric.absorcao)
    if call.data == 'ext':
        bot.send_message(call.message.chat.id, teoric.exaustao)
    if call.data == 'liq':
        bot.send_message(call.message.chat.id, teoric.liquidez)
    if call.data == 'esc':
        bot.send_message(call.message.chat.id, teoric.escora)
    if call.data == 'ren':
        bot.send_message(call.message.chat.id, teoric.renovacao)
    if call.data == 'can':
        bot.send_message(call.message.chat.id, teoric.cancelamento)
    
    #ferramentas
    if call.data == 'time':
        bot.send_message(call.message.chat.id, teoric.times)
    if call.data == 'book':
        bot.send_message(call.message.chat.id, teoric.book)
    if call.data == 'dom':
        bot.send_message(call.message.chat.id, teoric.dom)
    if call.data == 'vol':
        bot.send_message(call.message.chat.id, teoric.vol)
    if call.data == 'vwap':
        bot.send_message(call.message.chat.id, teoric.vwap)
    if call.data == 'ajuste':
        bot.send_message(call.message.chat.id, teoric.ajuste)
        
        #Psicologia 
    if call.data == 'ansiedade':
        msg = bot.send_message(call.message.chat.id, teoric.ansiedade)
        time(2, bot.delete_message, (msg.chat.id, msg.message_id).start)
    if call.data == 'medo':
        bot.send_message(call.message.chat.id, teoric.medo)
    if call.data == 'n_erros':
        bot.send_message(call.message.chat.id, teoric.n_erros)
    if call.data == 'sabotagem':
        bot.send_message(call.message.chat.id, teoric.sabotagem)
    if call.data == 'n_perder':
        bot.send_message(call.message.chat.id, teoric.n_perder)
    if call.data == 'n_ganhar':
        bot.send_message(call.message.chat.id, teoric.n_ganhar)
    if call.data == 'p_dinheiro':
        bot.send_message(call.message.chat.id, teoric.p_dinheiro)
    if call.data == 'n_estudar':
        bot.send_message(call.message.chat.id, teoric.n_estudar)
    if call.data == 'n_metas':
        bot.send_message(call.message.chat.id, teoric.n_metas)
    if call.data == 'inseguranca':
        bot.send_message(call.message.chat.id, teoric.inseguranca)

        #Informações
    if call.data == 'rules':
        bot.send_message(call.message.chat.id, teoric.rules)
    if call.data == 'replay':
        bot.send_message(call.message.chat.id, teoric.replay)
    if call.data == 'lista':
        bot.send_message(call.message.chat.id, teoric.lista)
    if call.data == 'vinho':
        bot.send_message(call.message.chat.id, teoric.vinho)


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
    
