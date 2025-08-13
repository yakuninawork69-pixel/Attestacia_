import telebot
from telebot import types
from request import gpt_request

def giga(message):
    bot.send_message(message.chat.id,gpt_request(message.text))
    return


bot = telebot.TeleBot(open(r'C:\Users\User\Desktop\Учеба_ИИ\Практика 7.1_ИИ\api.txt').read()) #Инициализация бота

btn1 = types.KeyboardButton('Расписание') #создание кнопки
btn2 = types.KeyboardButton('ДЗ')
btn3 = types.KeyboardButton('Фото')
btn4 = types.KeyboardButton('Вопрос GigaChat')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #сетка для кнопок
markup.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands=['start']) #определение реакции бота на /start
def send_wecome(message): #функция реакции на /start
    bot.reply_to(message, "Привет! Я учебный бот") #тело бота
    bot.send_message(message.chat.id, "Выберите действие:",
                     reply_markup=markup)

@bot.message_handler(func=lambda message:True) #блок обработки текстовых сообщений
def handler_buttons(message): #в эту фун-ю добавляем обработку текста через elif
    if message.text == 'Расписание':
        ph = open(r'C:\Users\User\Desktop\Учеба_ИИ\Практика 7.1_ИИ\Расписание.jpg','rb') #путь к фото, тип чтения. rb - читать файл
        bot.send_photo(message.chat.id,ph,'Расписание')
        ph.close()
        # url = 'https://i.calameoassets.com/140618095215-7633367e4b88d1195c48bde766f0dcaa/large.jpg'
        # bot.send_photo(message.chat.id,url,'Расписание')
        # bot.reply_to(message, "Сейчас лето, занятий нет.")
        # inline_markup = types.InlineKeyboardMarkup() #создание "шаблона" для инлайн кнопки
        # btn = types.InlineKeyboardButton( #текст и ссылка для кнопки и её инициализация
            # text="Летние активности",
           # url="https://leto.mos.ru/"
        # )
        # inline_markup.add(btn) #добавление кнопки в "шаблон" для инлайн кнопок
        # bot.send_message(message.chat.id, "Лучше посмотри летние активности", 
        #                 reply_markup=inline_markup) #отправка сообщения пользователю с кнопкой

    elif message.text =='ДЗ':
        doc = open(r'C:\Users\User\Desktop\Учеба_ИИ\Практика 7.1_ИИ\Это домашнее задание.pdf','rb')
        bot.send_document(message.chat.id,doc,caption='ДЗ', 
                          visible_file_name='Домашка.pdf')
        # bot.reply_to(message, "У вас каникулы, а всё ДЗ у учителей.")
    elif str(message.text).lower() =='привет':
        bot.reply_to(message, "Привет!")
    elif message.text == 'Фото':
        try:
            ph = open('name_file.jpg','rb') #путь к фото, тип чтения. rb - читать файл
            bot.send_photo(message.chat.id,ph,'Ваше последнее фото')
        except BaseException:
            bot.reply_to(message, "Фото отсуствует, отправьте новое.")
    elif message.text == 'Вопрос GigaChat':
        msg = bot.reply_to(message, "Напиши текст запроса для языковой модели")
        bot.register_next_step_handler(msg, giga)

@bot.message_handler(content_types=['photo'])
def photoes(message):
    file_id = message.photo[-1].file_id #из полученного сообщения берём фото. 
    # ИД хранится в последнем элементе с помощью обращения к нему мы получаем file id
    file_info = bot.get_file(file_id) #получение информации о самом файле по его ID
    download_file = bot.download_file(file_info.file_path) #загузка файла в оперативную память
    with open('name_file.jpg', 'wb') as new_f: #сохранение файла
        new_f.write(download_file)
    bot.reply_to(message,'Фото сохранено') #отправка уведомления пользователю





bot.polling() #отправка настроек в бот и его активация. 
#Без него бот неактивен

