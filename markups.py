from telebot import types
from Scripts import SQLite as sql

start_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
start_markup_btn1 = types.KeyboardButton('/start')
start_markup.add(start_markup_btn1)

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_btn1 = types.KeyboardButton('Случайная картинка')
source_markup_btn2 = types.KeyboardButton('Домашние задания')
source_markup_btn3 = types.KeyboardButton('Выход')
source_markup_btn4 = types.KeyboardButton('Выход')
source_markup_btn5 = types.KeyboardButton('Выход')
source_markup.add(source_markup_btn1,source_markup_btn2,
source_markup_btn3,source_markup_btn4,
source_markup_btn5)

homework_markups = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
list_subjects = sql.SelectMore("select * from subject")
for item in list_subjects:
    homework_markups.add(types.KeyboardButton(item[1]))

def initNames():
    return [item[1].lower() for item in list_subjects]