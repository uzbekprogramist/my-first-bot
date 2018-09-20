# -*- coding: utf-8 -*-

import telebot
import configparser
from other.another import just_print

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["DEFAULT"]["Token"])


@bot.message_handler(func=lambda message: message.text == config["Bot Specific"]["answer message"])
def reply_to(message):
    bot.send_message(message.chat.id, "Hello there!")


def main():
    print(just_print())
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
    C:\Python35\python.exe -m zipapp "D:\plase do not delete this fayl\my projects Anonim\For creat bots\my first bot" -m bot:main -o mybot.pyz.