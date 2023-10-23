import os
import telebot
from telebot import types
from users.models import User


def telegram_bot():
    telegram_token = os.getenv('TELEGRAM_BOT_API')
    bot = telebot.TeleBot(telegram_token)

    @bot.message_handler(commands=['start'])
    def send_message(message: types.Message):
        bot.send_message(message.chat.id, 'Добро пожаловать! Этот бот поможет вам сформировать ваши привычки!')
        bot.send_message(message.chat.id, 'Введите свой Email:')
        bot.register_next_step_handler_by_chat_id(message.chat.id, get_email)

        # user = User.objects.filetr(email=).fisrst()

    def get_email(message: types.Message):
        user = User.objects.filter(email=message.text).first()
        bot.send_message(message.chat.id, 'Введите свой пароль:')
        bot.register_next_step_handler_by_chat_id(message.chat.id, get_password, user)

    def get_password(message: types.Message, args):
        user = args
        check_password = user.check_password(message.text)
        if check_password:
            pass
        bot.send_message(message.chat.id, f'{check_password}')

    bot.polling(none_stop=True)
