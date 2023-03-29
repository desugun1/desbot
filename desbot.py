from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import time
import schedule
import telebot


TOKEN = "5431508902:AAH7rkF6TAOsZYZaDXgpkix4cj8s9R9pJBo"
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Новая задача'))
keyboard.add(KeyboardButton('Все задачи'))
sl = []


def job1(message):
    bot.send_message(message.chat.id, sl[0])


def job():
    c = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    schedule.every().c[sl[1][0]].at(sl[0]).do(job1)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Бот приветствует вас', reply_markup=keyboard)


@bot.message_handler(regexp=r'Новая задача')
def new_task(message):
    bot.send_message(message.chat.id, 'Введите новую задачу')
@bot.message_handler(content_types=["text"])
def newbie(message):
    sl.append(message.text)
    bot.send_message(message.chat.id, 'Назначьте время в формате день недели и время ЧЧ:ММ')
@bot.message_handler(content_types=["text"])
def newbie(message):
    sl.append(message.text)
    bot.send_message(message.chat.id, 'Отлично! Напоминание будет' + sl[1])
    job()
    schedule.cancel_job(job)


@bot.message_handler(func=lambda x: 'Все задачи' in x.text)
def send_text(message):
    bot.send_message(message.chat.id, *sl)


bot.infinity_polling()