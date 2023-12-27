from telebot import types
import TOKEN
import telebot
import random


bot = telebot.TeleBot(TOKEN.bot_token)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('🦅'), types.KeyboardButton('🪙'))
    bot.reply_to(message, "Добро пожаловать в игру 'Орел и Решка'! Для игры используйте кнопки:", reply_markup=markup)
@bot.message_handler(commands=['start'])

# def start_message(message):
#     bot.send_message(message.chat.id, "Выбери Орел или Решка?")

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == '🦅':
        list=["Ты выиграл, выпал Орел", "Ты проиграл, выпала Решка"]
        bot.send_message(message.chat.id,(random.choice(list)))

    elif message.text.lower() == '🪙':
        list=["Ты выиграл, выпала Решка", "Ты проиграл, выпал Орел"]
        bot.send_message(message.chat.id,(random.choice(list)))
    else:
        list=['Неправильное значение']
        list2=['Выберите Орел или Решка!']
        bot.send_message(message.chat.id,(list))
        bot.send_message(message.chat.id,(list2))

bot.polling()
