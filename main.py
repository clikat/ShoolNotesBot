import time
import sqlite3
import telebot

bot = telebot.TeleBot("7756654184:AAEA4VJeseSlQBEsw0tYNO_npT_agqoMjhc")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здраствуйте, это телеграмм бот созданный для Школы №60 Ростова-на-Дону. Создан: @qkodoku и @tyrytuty")