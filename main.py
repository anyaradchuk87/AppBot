import telebot
from telebot import types

bot = telebot.TeleBot('5535732977:AAGBPfXThCvnWoQNOkq5uMKtbaABuMSR85Y')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow, cool photo!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Wikipedia', url='https://wikipedia.ua'))
    bot.send_message(message.chat.id, 'Visited site', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Website')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'Hi there', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Your ID is {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('logo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I don\'t understand you', parse_mode='html')


bot.polling(none_stop=True)
