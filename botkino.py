import telebot
from telebot import types
import random

TOKEN = "7540140019:AAG7heZuusDAw-P9NQoukiRvQjKkIzbpbWw"
bot = telebot.TeleBot(TOKEN)

mas_sci_fi = ["«Сквозь снег»","«Лайк?»","«Поле битвы: Падение мира»","«Четвёртый вид» "]
mas_uhzas = ["«Ночь живых мертвецов» ","«Суспирия»","«Кошмар на улице Вязов»","«Ведьма из Блэр: Курсовая с того света» "]
mas_boevik = ["«Крепкий орешек»","«Форсаж»","«Телохранитель киллера»","Рэмпейдж"]
mas_komedi = ["«Бабушка на миллион»","«Сотни бобров»","«Миссия: Красный»","«Воображаемые друзья»"]

@bot.message_handler(commands = ["start"])
def start(msg):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    boevik = types.KeyboardButton("🔫 Боевик")
    komedia = types.KeyboardButton("🤣 Комедия")
    fantastika = types.KeyboardButton("👽 Фантастика")
    yjasi = types.KeyboardButton("👻 Ужасы")
    restart = types.KeyboardButton("🤖 Перезапустить бота")
    mrk.add(boevik, komedia, fantastika, yjasi, restart)
    bot.send_message(
        msg.chat.id,
        "Привет! Я бот, в котором ты можешь выбрать фильм на любой вкус! /n /n Выбирай жанр ниже 👇",
        reply_markup=mrk
    )

@bot.message_handler(content_types = ["text"])
def buttons(msg):
    film_b = random.choice(mas_boevik)
    if msg.text == "🔫 Боевик":
        bot.send_message(
            msg.chat.id,
            f"Предлагаю посмотреть фильм", film_b, "жанра Боевик"
        )

    film_k = random.choice(mas_komedi)
    if msg.text == "🤣 Комедия":
        bot.send_message(
            msg.chat.id,
            f"Предлагаю посмотреть фильм", film_k, "жанра Комедия"
        )

    film_f = random.choice(mas_sci_fi)
    if msg.text == "👽 Фантастика":
        bot.send_message(
            msg.chat.id,
            f"Предлагаю посмотреть фильм", film_f, "жанра Фантастика"
        )

    film_y = random.choice(mas_uhzas)
    if msg.text == "👻 Ужасы":
        bot.send_message(
            msg.chat.id,
            f"Предлагаю посмотреть фильм", film_y, "жанра Ужасы"
        )

    if msg.text == "🤖 Перезапустить бота":
        start(msg)

bot.polling()
