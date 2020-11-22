import sqlite3
from threading import Thread
from time import sleep
from telebot import TeleBot, types

class Worker(Thread):
    def __init__(self, API_TOKEN):
        self.CONNECTION = sqlite3.connect("YOUR_DB_PATH") #It must be changed
        self.CURSOR = self.CONNECTION.cursor()
        self.API_TOKEN = API_TOKEN
        self.BOT = TeleBot(API_TOKEN)
        self.CURSOR.execute('SELECT * FROM your_db_table;') #It must be changed
        self.results = self.CURSOR.fetchall()
        self.TIME_TO_SLEEP = 1500 #This is my default value
        Thread.__init__(self)
    def run(self):
        while True:
            try:
                for row in self.results:
                    # This is my default db's table elements
                    # image | oldprice | price | title | url
                    sendMessage(self=self, image=row[1], old_price=float(row[2]), actually_price=float(row[3]), title=row[4], url=row[5])
                    sleep(self.TIME_TO_SLEEP)
                
            except Exception as e: #Generic exception catcher
                print()
                print(e)
                print("Oops!", e.__class__, "occurred.")
                print()

def sendMessage(self, image, old_price, actually_price, title, url): #It can be changed
    discount = (actually_price * 100) / old_price
    discount = 100.0 - discount
    textMessage = ('⚠️ AliExpress Offer ⚠️\n🟢 {} 🟢\n❌ Before: {:.2f} ❌\n✅ Now: {:.2f} ✅\n🔥 Discount: {:.2f}% 🔥\n👇 LINK 👇'.format(title, old_price, actually_price, discount)) #Text

    markup = types.InlineKeyboardMarkup() #Buttons
    markup.add(types.InlineKeyboardButton(text='💎 AliExpress 💎',
                                            url=url,
                                            callback_data=url))

    self.BOT.send_photo(chat_id='@YOUR_CHANNEL_ID', #Where do you want to send? Change it with your channel id | You can use a user id
                        photo=image,
                        caption=textMessage,
                        reply_markup=markup) #Set my finally message with photo, text and buttons, so send