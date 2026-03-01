import telebot
import os

TOKEN = "8694865950:AAFIx989It9Xrgxrgum7erEKLoAofeHQ7iM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hej 👋 Bot działa!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Napisałeś: " + message.text)

print("Bot działa...")
bot.infinity_polling()
