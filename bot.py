import telebot
from config import *
from db_logic import Bot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я бот по игре Honkai Star Rail, который может тебе рассказать информацию о каждом персонаже в игре.\n\nНапиши /Information чтобы узнать о игре получше.\nНапиши /Character чтобы посмотреть на детали твоего любимого персонажа."
    )

@bot.message_handler(commands=['Information'])
def handle_information(message):
    bot.send_message(
        message.chat.id,
        "Honkai: Star Rail — бесплатная пошаговая RPG-игра от HoYoverse, в которой игрок путешествует по разным мирам вместе с командой Astral Express, сражается с врагами, собирает персонажей и раскрывает тайны вселенной с помощью стратегической боевой системы, основанной на Пути и Элементах персонажей."
    )



@bot.message_handler(commands=['Character'])
def handle_character(message):
    msg = bot.send_message(
        message.chat.id,
        "Какого персонажа ты хочешь найти?"
    )

    bot.register_next_step_handler(msg, search_character)


def search_character(message):
    character_name = message.text

    character = Bot.get_character_info(character_name)

    if character == "Character not found!":
        bot.send_message(
            message.chat.id,
            "❌ Персонаж не найден."
        )
        return

    text = (
        f"⭐ {character['name']}\n\n"
        f"ID: {character['id']}\n"
        f"Редкость: {character['rarity']}★\n"
        f"Путь: {character['path']}\n"
        f"Элемент: {character['element']}\n"
        f"Фракция: {character['faction']}\n"
        f"Планета: {character['planet']}\n\n"
        f"{character['description']}"
    )

    bot.send_message(message.chat.id, text)


bot.polling()
