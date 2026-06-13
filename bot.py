import telebot
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот по игре Honkai Star Rail, который может тебе рассказать информацию о каждом персонаже в игре.\n\nНапиши /Information чтобы узнать о игре получше.\nНапиши /Character чтобы посмотреть на детали твоего любимого персонажа."
    )

@bot.message_handler(commands=['Information'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Honkai: Star Rail — бесплатная пошаговая RPG-игра от HoYoverse, в которой игрок путешествует по разным мирам вместе с командой Astral Express, сражается с врагами, собирает персонажей и раскрывает тайны вселенной с помощью стратегической боевой системы, основанной на Пути и Элементах персонажей."
    )

bot.polling()
