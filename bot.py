import telebot
from telebot import types
import settings

bot = telebot.TeleBot(settings.TG_TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "Привет! Выбирай🐹", reply_markup=keyboard)


# создание главных кнопок
def create_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    btn1 = types.InlineKeyboardButton(text="Смотреть фильм", callback_data='1')
    btn2 = types.InlineKeyboardButton(text="Заказать еду к фильму", callback_data='2')
    btn3 = types.InlineKeyboardButton(text="Сходить в кино", url='https://afisha.me/film/')
    keyboard.add(btn1, btn2, btn3)
    return keyboard


# создание кнопок с выбором
def film():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    btn4 = types.InlineKeyboardButton(text="Найти по названию", callback_data='4')
    btn5 = types.InlineKeyboardButton(text="Выбрать по жанру", callback_data='5')
    btn46 = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
    keyboard.add(btn4, btn5, btn46)
    return keyboard


# создание кнопок с жанрами
def style():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    btn6 = types.InlineKeyboardButton(text="Вестерны", url='https://rezka.ag/films/western/')
    btn7 = types.InlineKeyboardButton(text="Арт-хаус", url='https://rezka.ag/films/arthouse/')
    btn8 = types.InlineKeyboardButton(text="Криминал", url='https://rezka.ag/films/crime/')
    btn9 = types.InlineKeyboardButton(text="Фантастика", url='https://rezka.ag/films/fiction/')
    btn10 = types.InlineKeyboardButton(text="Ужасы", url='https://rezka.ag/films/horror/')
    btn11 = types.InlineKeyboardButton(text="Документальные", url='https://rezka.ag/films/documentary/')
    btn12 = types.InlineKeyboardButton(text="Познавательные", url='https://rezka.ag/films/cognitive/')
    btn13 = types.InlineKeyboardButton(text="Короткометражные", url='https://rezka.ag/films/short/')
    btn14 = types.InlineKeyboardButton(text="Семейные", url='https://rezka.ag/films/family/')
    btn15 = types.InlineKeyboardButton(text="Боевики", url='https://rezka.ag/films/action/')
    btn16 = types.InlineKeyboardButton(text="Приключения", url='https://rezka.ag/films/adventures/')
    btn17 = types.InlineKeyboardButton(text="Комедии", url='https://rezka.ag/films/comedy/')
    btn18 = types.InlineKeyboardButton(text="Мюзиклы", url='https://rezka.ag/films/musical/')
    btn19 = types.InlineKeyboardButton(text="Эротика", url='https://rezka.ag/films/erotic/')
    btn20 = types.InlineKeyboardButton(text="Театр", url='https://rezka.ag/films/theatre/')
    btn21 = types.InlineKeyboardButton(text="Наши", url='https://rezka.ag/films/our/')
    btn22 = types.InlineKeyboardButton(text="Фэнтэзи", url='https://rezka.ag/films/fantasy/')
    btn23 = types.InlineKeyboardButton(text="Военные", url='https://rezka.ag/films/military/')
    btn24 = types.InlineKeyboardButton(text="Драмы", url='https://rezka.ag/films/drama/')
    btn25 = types.InlineKeyboardButton(text="Мелодрамы", url='https://rezka.ag/films/melodrama/')
    btn26 = types.InlineKeyboardButton(text="Музыкальные", url='https://rezka.ag/films/musical/')
    btn27 = types.InlineKeyboardButton(text="Детские", url='https://rezka.ag/films/kids/')
    btn28 = types.InlineKeyboardButton(text="Концерт", url='https://rezka.ag/films/concert/')
    btn29 = types.InlineKeyboardButton(text="Украинские", url='https://rezka.ag/films/ukrainian/')
    btn30 = types.InlineKeyboardButton(text="Биографические", url='https://rezka.ag/films/biographical/')
    btn31 = types.InlineKeyboardButton(text="Детективы", url='https://rezka.ag/films/detective/')
    btn32 = types.InlineKeyboardButton(text="Спортивные", url='https://rezka.ag/films/sport/')
    btn33 = types.InlineKeyboardButton(text="Триллеры", url='https://rezka.ag/films/thriller/')
    btn34 = types.InlineKeyboardButton(text="Исторические", url='https://rezka.ag/films/historical/')
    btn35 = types.InlineKeyboardButton(text="Путешествия", url='https://rezka.ag/films/travel/')
    btn36 = types.InlineKeyboardButton(text="Стендап", url='https://rezka.ag/films/standup/')
    btn37 = types.InlineKeyboardButton(text="Зарубежные", url='https://rezka.ag/films/foreign/')
    btn38 = types.InlineKeyboardButton(text="Новинки HBO", url='https://rezka.ag/collections/1419-filmy-hbo/')
    btn39 = types.InlineKeyboardButton(text="Новинки NETFLIX",
                                       url='https://rezka.ag/collections/834-filmy-netflix/')
    btn46 = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
    keyboard.add(btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20,
                 btn21, btn22, btn23, btn24, btn25, btn26, btn27, btn28, btn29,btn30, btn31, btn32, btn33, btn34, btn35,
                 btn36, btn37, btn38, btn39, btn46)
    return keyboard

#наброски с поиск по названию
def search(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    a = message.text.lower()
    btn40 = types.InlineKeyboardButton(text='Нажимай',
                                       url=f'https://rezka.ag/search/?do=search&subaction=search&q=+{a}')
    btn46 = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
    keyboard.add(btn40, btn46)
    return keyboard

@bot.message_handler(content_types=['text'])
def write_world(message):
    key = search(message)
    nazv = message.text
    nazv.replace(' ', '+')
    bot.send_message(message.chat.id, f'Вы выбрали фильм {nazv}', reply_markup=key)



# создание кнопок с едой
def food():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    btn41 = types.InlineKeyboardButton(text='Суши',
                                       url='https://eda.yandex.by/minsk?quickfilter=sushi&shippingType=delivery')
    btn42 = types.InlineKeyboardButton(text='Пицца',
                                       url='https://eda.yandex.by/minsk?quickfilter=pizza&shippingType=delivery')
    btn43 = types.InlineKeyboardButton(text='Бургеры',
                                       url='https://eda.yandex.by/minsk?quickfilter=burger&shippingType=delivery')
    btn44 = types.InlineKeyboardButton(text='Десерты',
                                       url='https://eda.yandex.by/minsk?quickfilter=deserti&shippingType=delivery')
    btn45 = types.InlineKeyboardButton(text='Шаурма',
                                       url='https://eda.yandex.by/minsk?quickfilter=shaurma&shippingType=delivery')
    btn46 = types.InlineKeyboardButton(text='Вернуться назад', callback_data='6')
    keyboard.add(btn41, btn42, btn43, btn44, btn45, btn46)
    return keyboard


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard_1 = film()
    keyboard_2 = create_keyboard()
    keyboard_3 = style()
    keyboard_4 = food()
    if call.message:
        if call.data == '1':
            bot.send_message(call.message.chat.id,
                             'Отличный выбор, осталось определиться какой!',
                             reply_markup=keyboard_1)
        elif call.data == "2":
            bot.send_message(call.message.chat.id,
                             'Выберите еду',
                             reply_markup=keyboard_4)
        elif call.data == '6':
            bot.send_message(call.message.chat.id,
                             'Вы вернулись в главное меню',
                             reply_markup=keyboard_2)
        elif call.data == '4':
            bot.send_message(call.message.chat.id, 'Отправь мне название фильма')
        elif call.data == "5":
            bot.send_message(call.message.chat.id,
                             'Выберите жанр',
                             reply_markup=keyboard_3)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)