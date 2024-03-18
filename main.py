from telebot import types, TeleBot
import os
import random
import telebot


forma, design1, checkin10 = [], [], []


bot: TeleBot = telebot.TeleBot(
    '6963016657:AAFE0hI6za9QJKYIS_4PVcnSlyN5ENLHecY')


@bot.message_handler(commands=['start'])
def menu1(message):

    letsgo = types.InlineKeyboardMarkup()
    short = types.InlineKeyboardButton(
        "Выбрать маникюр", callback_data='nails')
    letsgo.row(short)

    check = types.InlineKeyboardButton('Записаться', callback_data='check')
    letsgo.row(check)

    address = types.InlineKeyboardButton('Адрес', callback_data='address')
    letsgo.row(address)

    feedback = types.InlineKeyboardButton(
        'Оставить отзыв', callback_data='feedback')
    letsgo.row(feedback)

    contacts = types.InlineKeyboardButton('Контакты', callback_data='contacts')
    letsgo.row(contacts)

    bot.send_message(
        message.chat.id, "Привет, это наш маникюр-бот. Начнем?", reply_markup=letsgo)


@bot.callback_query_handler(func=lambda callback: True)
def menu(callback):
    if callback.data == 'nails':
        length = types.ReplyKeyboardMarkup(resize_keyboard=True)
        short = types.KeyboardButton("Короткие")
        length.row(short)
        long = types.KeyboardButton("Длинные")
        length.row(long)
        bot.send_message(callback.message.chat.id,
                         "Выбери длину", reply_markup=length)
        bot.register_next_step_handler(callback.message, formanails)

    elif callback.data == 'check':
        windows = open('images/windowsdef1.jpg', 'rb')
        bot.send_message(callback.message.chat.id, 'Посмотри окошки и напиши подходящее время',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(callback.message.chat.id, windows)
        bot.register_next_step_handler(callback.message, checkin2)

    elif callback.data == 'address':
        back = types.InlineKeyboardButton('Назад', callback_data='menu')
        back_markup = types.InlineKeyboardMarkup().add(back)
        address_message = "Мы находимся по адресу : Пр. Ленина 154, корпус 3, стеклянный вход, перед паребриком налево \n<a href='https://yandex.ru/maps/10716/balashiha/geo/mikrorayon_olgino/1612744559/?ll=37.986017%2C55.743261&z=15.31'>Посмотреть на карте</a>"
        bot.send_message(callback.message.chat.id, address_message,
                         parse_mode='HTML', reply_markup=back_markup)

    elif callback.data == 'feedback':
        back = types.InlineKeyboardMarkup()
        backbtn = types.InlineKeyboardButton(
            'Вернуться в меню', callback_data='menu')
        back.row(backbtn)
        bot.send_message(callback.message.chat.id,
                         "Здесь ты можешь написать отзыв по нашей работе",
                         reply_markup=back)
        bot.register_next_step_handler(callback.message, feedback2)

    elif callback.data == 'contacts':
        back = types.InlineKeyboardMarkup()
        backbtn = types.InlineKeyboardButton(
            'Вернуться в меню', callback_data='menu')
        back.row(backbtn)
        bot.send_message(callback.message.chat.id, 'Вконтакте: https://vk.com/am.stage \n'
                                                   'Телеграмм-канал: https://web.telegram.org/a/#6324719377 \n')

    elif callback.data == 'more':
        if cpt > 1:
            pic = open('images/' + allp + '/' +
                       str(random.randint(1, cpt)) + '.jpg', 'rb')
        else:
            pic = open('images/' + allp + '/1.jpg', 'rb')

        menu = types.InlineKeyboardMarkup()
        more = types.InlineKeyboardButton('Еще!', callback_data='more')
        menu.row(more)
        want = types.InlineKeyboardButton('Записаться', callback_data='check')
        menu.row(want)
        again = types.InlineKeyboardButton("Сначала", callback_data='again')
        menu.row(again)
        menu2 = types.InlineKeyboardButton("Меню", callback_data='menu')
        menu.row(menu2)

        bot.send_photo(callback.message.chat.id, pic, reply_markup=menu)

    elif callback.data == 'menu':
        letsgo = types.InlineKeyboardMarkup()
        short = types.InlineKeyboardButton(
            "Выбрать маникюр", callback_data='nails')
        letsgo.row(short)

        check = types.InlineKeyboardButton('Записаться', callback_data='check')
        letsgo.row(check)

        address = types.InlineKeyboardButton('Адрес', callback_data='address')
        letsgo.row(address)

        feedback = types.InlineKeyboardButton(
            'Оставить отзыв', callback_data='feedback')
        letsgo.row(feedback)

        bot.send_message(callback.message.chat.id, "Меню", reply_markup=letsgo)

    else:
        pass


def formanails(message):
    global forma
    forma = [message.text]
    form = types.ReplyKeyboardMarkup(resize_keyboard=True)
    square = types.KeyboardButton("Квадратная")
    form.row(square)
    almond = types.KeyboardButton("Миндалевидная")
    form.row(almond)
    pic = open('images/form.jpg', 'rb')
    bot.send_photo(message.chat.id, pic)
    bot.send_message(message.chat.id, 'Выбери форму', reply_markup=form)
    bot.register_next_step_handler(message, color)


def color(message):

    forma.append(message.text)
    colors = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vivid = types.KeyboardButton("Яркий")
    colors.row(vivid)
    nude = types.KeyboardButton("Нюд")
    colors.row(nude)

    bot.send_message(message.chat.id,
                     'Выбери цвет',
                     reply_markup=colors)

    bot.register_next_step_handler(message, design)


def design(message):

    forma.append(message.text)
    design_list = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nope = types.KeyboardButton('Без дизайна')
    design_list.row(nope)
    french = types.KeyboardButton('Френч')
    design_list.row(french)
    glitter = types.KeyboardButton("Блестки")
    design_list.row(glitter)
    hard = types.KeyboardButton("Сложный дизайн")
    design_list.row(hard)
    bot.send_message(message.chat.id, 'Выбери дизайн',
                     reply_markup=design_list)

    bot.register_next_step_handler(message, ready)


def ready(message):
    design1 = message.text
    forma_str = "/".join(forma)
    design1_str1 = ''.join(design1)
    global allp, cpt

    allp = forma_str + '.' + design1_str1
    cpt = sum([len(files) for r, d, files in os.walk(
        "C:\\Users\\Mikhail\\Downloads\\Нужное\\Ксюша\\Программирование\\PycharmProjects\\nails-bot\\images\\"+allp)])
    if cpt > 1:
        pic = open('images/' + allp + '/' +
                   str(random.randint(1, cpt)) + '.jpg', 'rb')
    else:
        pic = open('images/' + allp + '/1.jpg', 'rb')

    menu = types.InlineKeyboardMarkup()
    more = types.InlineKeyboardButton('Еще!', callback_data='more')
    menu.row(more)
    want = types.InlineKeyboardButton('Записаться', callback_data='check')
    menu.row(want)
    again = types.InlineKeyboardButton("Сначала", callback_data='nails')
    menu.row(again)
    menu2 = types.InlineKeyboardButton("Меню", callback_data='menu')
    menu.row(menu2)
    bot.send_photo(message.chat.id, pic, reply_markup=menu)


def checkin2(message):
    bot.send_message(message.chat.id, 'Напиши свое имя и номер телефона')
    checkin10 = message.text
    bot.send_message(224008722, checkin10)
    bot.register_next_step_handler(message, checkin3)


def checkin3(message):
    checkin11 = message.text

    bot.send_message(224008722, checkin11)
    back = types.InlineKeyboardMarkup()
    backbtn = types.InlineKeyboardButton(
        'Вернуться в меню', callback_data='menu')
    back.row(backbtn)
    bot.send_message(
        message.chat.id, 'Ты записана! Скоро с тобой свяжется менеджер для подтверждения записи)', reply_markup=back)


def feedback2(message):
    back = types.InlineKeyboardMarkup()
    backbtn = types.InlineKeyboardButton(
        'Вернуться в меню', callback_data='menu')
    back.row(backbtn)
    feedback = message.text
    bot.send_message(224008722, feedback)
    bot.send_message(message.chat.id,
                     "Спасибо за твой отзыв! Мы обязательно его прочитаем и дадим обратную связь",
                     reply_markup=back)


bot.polling(none_stop=True)
