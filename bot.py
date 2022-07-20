from tkinter import Menu
import telebot
import markups as m
from Task import Task
from Scripts.Menu import HomeWorks as hw
from Scripts import RndImage as RI
from Scripts import SQLite as sql

token = open("token", 'r').read()
bot = telebot.TeleBot(token)
task = Task()
task.homeworks = m.initNames()
print(task.homeworks)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    if not task.isRunning:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Привет')
        msg = bot.send_message(chat_id, 'Выбери команду', 
        reply_markup=m.source_markup)
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
    elif text in task.names[2]:
        msg = bot.send_message(chat_id, "И что же тебя интересует?", reply_markup=m.homework_markups)
        bot.register_next_step_handler(msg, hw.askSubject)
        # result_sql = sql.SelectOne("select Decision from tasks where id == 1")
        # msg = bot.send_message(chat_id, "```\r\n" + result_sql + "```", parse_mode="Markdown")
        # bot.register_next_step_handler(msg, askAction)
        

bot.polling()