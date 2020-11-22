from telebot import TeleBot, types  # Api Telegram
from time import sleep
import csv
import sqlite3
from worker import Worker #look at worker.py

API_TOKEN = 'YOUR_API' #It must be changed
BOT = TeleBot(API_TOKEN)

@BOT.message_handler(commands=['start'])
def send_message(message):
    if message.from_user.username == 'YOUR_USERNAME':  #It must be changed
        One = Worker(API_TOKEN="YOUR_API") #It must be changed
        One.start()
        
        #Two = Worker(API_TOKEN="YOUR_API")
        #Two.start()
        
        #Three = Worker(API_TOKEN="YOUR_API")
        #Three.start()

BOT.polling()