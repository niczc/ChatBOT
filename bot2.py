from typing import KeysView
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

stringList = {"Absorcao": 'muito lote, pouco resultado', "Exaustao": 'Pouco lote, muito resultado'}
crossIcon = u"\u274C"
def makeKeyboard():
    markup = types.InlineKeyboardMarkup()
    
    for key, value in stringList.items():
        markup.add(types.InlineKeyboardButton(text = value,callback_data="['value', '" + value + "', '" + key + "']")),
        types.InlineKeyboardButton(text=crossIcon, callback="['Key', '" + key + "']")
    return markup 
        

@bot.message_handler(commands=['start'])
def menu_principal(message): 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Operacionais', callback_data = 'sub_Menu'),
        telebot.types.InlineKeyboardButton('Ferramentas', callback_data = 'None')
    )
    
        
    keyboard.row(
        telebot.types.InlineKeyboardButton('Psicologia do Trader', callback_data= 'None'),
        telebot.types.InlineKeyboardButton('Youtube', url = 'https://youtube.com/olhonoreplay')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Informações', callback_data= 'None')
    )
    bot.send_message(message.chat.id, 'Olá, eu sou o Doleta. Precisa de ajuda? ', reply_markup=keyboard)
    

@bot.message_handler(commands=['sub_Menu'])
def menu_operacionais(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Absorção', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Exaustao', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Lote de Liquidez', callback_data = 'abs')
    )    
    keyboard.row(
        telebot.types.InlineKeyboardButton('Lote de Escora', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Renovação', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Cancelamento', callback_data = 'abs')
    )
    bot.send_message(message.chat.id, 'Operacionais de Tape Reading ', reply_markup=keyboard)

@bot.message_handler(commands=['sub_Menu2'])
def menu_ferramentas(message):
    #ADICIONAR FOTOS
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Times & Trades', callback_data = 'abs')
    )   
    keyboard.row(
        telebot.types.InlineKeyboardButton('Book de Ofertas', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Super DOM', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Volume At Price', callback_data = 'abs')
    )
    bot.send_message(message.chat.id, 'Ferramentas de Tape Reading ', reply_markup=keyboard)

@bot.message_handler(commands=['sub_menu3'])
def menu_psicologia(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Ansiedade', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Medo', callback_data = 'abs')
    )    
    keyboard.row(
        telebot.types.InlineKeyboardButton('Não aceita os erros', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Auto Sabotagem', callback_data = 'abs')
    ) 
    keyboard.row(
        telebot.types.InlineKeyboardButton('Não sabe perder', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Não sabe ganhar', callback_data = 'abs')
    )        
    keyboard.row(
        telebot.types.InlineKeyboardButton('Pressa em ganhar dinheiro', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Não ter paciencia pra estudar', callback_data = 'abs')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Não saber traçar metas e objetivos', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Insegurança', callback_data = 'abs')
    )
    bot.send_message(message.chat.id, 'Psicologia do Trader ', reply_markup=keyboard)

@bot.message_handler(commands=['sub_menu4'])
def menu_informacoes(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Regras do Grupo', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Canal do Youtube', callback_data = 'abs')        
    ) 
    keyboard.row(
        telebot.types.InlineKeyboardButton('Replay do Dia', callback_data = 'abs'),
        telebot.types.InlineKeyboardButton('Lista dos Replays', callback_data = 'abs')        
    )  
    bot.send_message(message.chat.id, 'Informações do Grupo', reply_markup=keyboard)

   
@bot.message_handler(commands=['help'])
def send_message(message):
    bot.reply_to(message, "Está precisando de ajuda?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True)
