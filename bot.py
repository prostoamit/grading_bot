import telebot, os, random
from telebot import types

bot = telebot.TeleBot('1341076858:AAE-I9UzsC6lNG4B2aCsgiFGrPLC5gIef6E')
photos = './photos/'


@bot.message_handler(commands=['start'])
def startup(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    random_photo = types.KeyboardButton('Рандомная тупая фотка')

    markup.add(random_photo)

    bot.send_message(message.chat.id, "Welcome, <b>{0.first_name}</b>!".format(message.from_user), parse_mode='html', reply_markup=markup)
    print('somewone\'s using your bot. Name {0}\n'.format(message.from_user.first_name))


@bot.message_handler(content_types=['text'])
def reaction(message):
    if message.text == 'Рандомная тупая фотка':
        photo_path = random.choice(os.listdir(photos))

        meme = open(photos+photo_path, 'rb')

        bot.send_photo(message.chat.id, meme)

    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
