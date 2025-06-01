import telebot
from telebot import types

TOKEN = "7540140019:AAG7heZuusDAw-P9NQoukiRvQjKkIzbpbWw"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def start(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    mrk.add()
    bot.send_message(
        msg.chat.id,
        "Привет! Я бот, в котором ты можешь выбрать фильм на любой вкус! /n /n Выбирай жанр ниже 👇",
        reply_markup=mrk
    )