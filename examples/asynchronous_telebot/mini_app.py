import telebot

API_TOKEN = '7583741383:AAGf1J5Y4ja5tUxQsfvmQUpR07D1gJ1rz6M'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])#/start
def start(message):
    bot.reply_to(message, '{username}您好！👻我是嘉宝机器人🦋')

@bot.message_handler(commands=['start'])#/start
def start(message):
    bot.reply_to(message, '{username}您好！👻我是嘉宝机器人🦋')
    
@bot.message_handler(commands=['帮助'])#/帮助
def 帮助(message):
    bot.reply_to(message, '我能帮上什么忙？')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def Super(message):
    if message =='Super':
        print('Super info')


bot.infinity_polling()
