import telebot
import wikipedia
import re

bot = telebot.TeleBot('5535732977:AAGBPfXThCvnWoQNOkq5uMKtbaABuMSR85Y')

wikipedia.set_lang('en')


def get_wiki(word):
    try:
        ny = wikipedia.page(word)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if len(x.strip()) > 3:
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'There is no information in wiki about this'


@bot.message_handler(commands=['start'])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Send me word and I\'ll find information')


@bot.message_handler(content_types=['text'])
def get_user_photo(message):
    bot.send_message(message.chat.id, get_wiki(message.text))


bot.polling(none_stop=True, interval=0)
