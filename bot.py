import telebot
import markups as m
from Scripts import RndImage as RI
from Task import Task

token = open("token", 'r').read()
bot = telebot.TeleBot(token)
task = Task()

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Привет')
        msg = bot.send_message(chat_id, 'Выбери команду', reply_markup=m.source_markup)
        bot.register_next_step_handler(msg, askAction)
        task.isRunning = True

def askAction(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text in task.names[0]:
        msg = bot.send_message(chat_id, "Выходим", reply_markup = m.start_markup)
        task.isRunning = False
        bot.register_next_step_handler(msg, start_handler)
    elif text in task.names[1]:
        img = open(RI.GetRndImage(), 'rb')
        msg = bot.send_photo(chat_id, photo=img)
        bot.register_next_step_handler(msg, askAction)

bot.polling()
