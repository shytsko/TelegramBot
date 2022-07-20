import telebot
from Task import Task
import markups as m

def initBot(_bot, taskClass):
    global bot 
    bot = _bot
    global task
    task = taskClass

def askSubject(message):
    chat_id = bot.message.chat.id
    text = message.text.lower()
    