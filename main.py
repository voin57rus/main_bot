import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

print('Бот в работе!')
     

# Запуск бота
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    item2 = types.KeyboardButton('Важное')
    item3 = types.KeyboardButton('Информация')
    item4 = types.KeyboardButton('Разное')
    item7 = types.KeyboardButton('Ваши отзывы')
    markup.add(item2,  item3, item4, item7)
    


# Приветственное сообщения
    bot.send_message(message.chat.id, '<b>Привет мой дорогой друг   {0.first_name} ! \n Вас приветствует группа Alteza-Hack </b>👏\n\n <i>Вот не большое меню на кнопках!</i>'.format(message.from_user), parse_mode= 'HTML', reply_markup = markup)

#  инлайн кнопка
@bot.message_handler(content_types = ['site'])
def def_message(message):
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('', url= 'https://bombosait.ru'))
    # bot.reply_to(message, 'сайт', reply_markup=markup)



@bot.message_handler(content_types = ['text'])
def main(message, reply_markup=None):
    id = message.chat.id
    msg = message.text.lower()
    text = message.text.lower()

# Важные условия   
    if message.text == 'Важное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Прочитать')               
            back = types.KeyboardButton('Назад')
            markup.add(item1,  back)
            bot.send_message(message.chat.id, 'Правила прошу прочитать ❗❗❗', reply_markup = markup)

#  ваши отзывы
    elif message.text == 'Ваши отзывы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item7 = types.KeyboardButton('Напишите')
            back = types.KeyboardButton('Назад')
            # markup.add(item7,back)
            bot.send_message(id, "<b>Напишите пожалуйства Ваш отзыв!\n О работе групп и сайта!</b> \n(и если не трудно свой ник) \n<i>Я думаю Вам не составить труда перейти</i> <b>\n по ссылке ниже</B> 👇\n\n https://bombosait.ru/topic/29-отзывы-об-Alteza_hack", parse_mode= 'HTML',reply_markup = markup)



# Информация чита        
    elif message.text == 'Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Установи')
            item2 = types.KeyboardButton('Скачать хак')
            item3 = types.KeyboardButton('Новости хака')
            item4 = types.KeyboardButton('Цены')
            item5 = types.KeyboardButton('Реквизиты')
            item6 = types.KeyboardButton('Как приобрести')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)
            bot.send_message(message.chat.id, 'Информация', reply_markup = markup)

# Разное меню
    elif message.text == 'Разное':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Видеообзор')
            item2 = types.KeyboardButton('Группы')
            item3 = types.KeyboardButton('Сайт')
            item4 = types.KeyboardButton('Для личного общения')
            item5 = types.KeyboardButton('Запуск  Alteza_Hack')
            back = types.KeyboardButton('Назад')
            markup.add(item4, item3,item2, item1, item5, back)
            bot.send_message(message.chat.id, 'Разное', reply_markup = markup)

# Возврощения на зад       
    elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item2 = types.KeyboardButton('Важное')
            item3 = types.KeyboardButton('Информация')
            item4 = types.KeyboardButton('Разное')
            item7 = types.KeyboardButton('Ваши отзывы')
            markup.add(item2,item3, item4, item7)
            bot.send_message(message.chat.id, 'Назад', reply_markup = markup)




# Ваши отзывы            
    # elif msg == 'напишите':
    #      bot.send_message(id, "<b>Напишите пожалуйства Ваш отзыв!</b> <i> О работе групп и сайта (и если не трудно свой ник) перейдя по ссылке ниже</i> 👇\n\n https://bombosait.ru/topic/29-отзывы-об-Alteza_hack", parse_mode= 'HTML')
 

# Видеообзор чита       
    elif msg == 'видеообзор':
        bot.send_message(id,  "Не большая настройка как играть с [FaSt_AiM]можно посмотреть здесь  ➡️   https://bombosait.ru/forum/30-гайды-советы-по-игре")



# Инфа о чите
    elif msg == 'новости хака':
        bot.send_photo(id, "https://sun9-71.userapi.com/impg/JtWa5PwQTV2hIiBSdl14ytUqsHw59cwUXi7-6A/8sq-5SQABI8.jpg?size=1600x971&quality=95&sign=34cf7148443185d5bf6ef343bfe351ee&type=album", "Всем привет друзья мои❗\nС праздником 23 февраля❗\nИ в честь праздника - сегодня вам будет подарок❗\nКто приобретёт Hack❗\nНа три дня - день в подарок.\nНа семь дней - два в подарок.\nНе упустите свой шанс - всё закончится 25.03.2020 ❗")
   
# Скачать чит
    elif msg == 'скачать хак':
        # bot.send_photo(id, "https://bombosait.ru/bombo/sitee.jpg", "👇\n\nhttps://www.upload.ee/files/8996882/AltezaUpdate.rar.html")
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Жми на кнопку скачать:  Alteza_Hack', url= 'https://www.upload.ee/files/8996882/AltezaUpdate.rar.html'))
        bot.send_photo(id, 'https://bombosait.ru/bombo/sda.jpg', reply_markup=markup)

# Нет меню    
    elif msg == 'установи':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Скачай и установи❗️', url= 'https://www.upload.ee/files/14749523/____________.rar.html'))
        bot.send_photo(id, 'https://bombosait.ru/bombo/skin.png','Если есть такая ошибка .... или другие при запуске Хака ❗️', reply_markup=markup)
        # bot.send_message(id, "Если есть такая ошибка .... или другие при запуске Хака ❗️")

# Правила покупки
    elif msg == 'прочитать':
        bot.send_video(id, "https://tenor.com/view/%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%D1%87%D0%B8%D1%82%D0%B0%D0%B9%D0%B0%D0%B1%D0%BE%D0%B1%D0%B0%D0%BD-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D1%87%D0%B8%D1%82%D0%B0%D0%B9-%D0%B0%D0%B1%D0%BE-%D0%B1%D0%B0%D0%BD-gif-26191291")
        bot.send_message(id, "❗Всем читать   👇\nhttps://bombosait.ru/bombo/important.txt")


# Мои группы    
    elif msg == 'группы':
        bot.send_photo(id, "https://bombosait.ru/bombo/re.jpg",  "Telegram_Group:  https://t.me/Alteza_Hack_Baresark  \n Telegram_Chat_Alteza hack:  https://t.me/+cOyHU6tXxQg2ODIy  \n Discord:  https://discord.gg/DasYCmqVk  \nVk:  https://vk.com/alteza_hack \nTeletype https://teletype.in/@oleg_57rus/UrM841gnndb\n Boosty  https://boosty.to/oleg_57rus")


# Запуск чита
    elif msg == 'запуск  alteza_hack':
        bot.send_photo(id, "https://bombosait.ru/bombo/aa.jpg", "<b>НЕ забываем отключить все защитники и антивирусы❗  Иначе Вы не сможете запустить чит ❗ \n И малая вероятность,что вы словите БАН❗️❗️❗️ \n\nЗапускаем игру до серверов ❕\nДалее делаем запуск Хака  от Админа ❕</b>\n\n<i>Меню в игре появится автоматом\n Закрыть меню на Home ❕</i>", parse_mode= 'HTML')

# Для личного общения 
    elif msg == 'для личного общения':
        bot.send_message(id, "https://t.me/Alteza_Hack")

#  Цены для хака       
    elif msg == 'цены':     
        bot.send_photo(message.chat.id, 'https://bombosait.ru/bombo/d.jpg',"Цены:\n1)день = 70р\n3)дня = 120р\n7)дней = 220р\n30)дней = 360р\n60)дней = 550р")
        bot.send_message(message.chat.id, "💸")

# Мой сайт
    elif msg == 'сайт':
        # bot.send_photo(id, "https://bombosait.ru/bombo/lk.jpg")
    #     bot.reply_to(message, 'https://bombosait.ru')
       markup = types.InlineKeyboardMarkup()
       markup.add(types.InlineKeyboardButton('Перейти на сайт', url= 'https://bombosait.ru'))
       bot.send_photo(id, 'https://bombosait.ru/bombo/lk.jpg', reply_markup=markup)


# Мои реквизиты
    elif msg == 'реквизиты':
        bot.send_photo(id, "https://bombosait.ru/bombo/vvv.jpg", "Tinkoff 2200 7001 2230 8439 \n\nкиви +79933719001\n\n https://yoomoney.ru/to/4100111524920305")

#  Как приобретать хак  
    elif msg == 'как приобрести':
        bot.send_photo(id, "https://bombosait.ru/bombo/bn.png","Вы оплачиваете кидаете ключик для активации❗\nЯ если на месте то активацию сделаю сразу❗\n Если меня нет на месте❗\nТо как приду всё сделаю❗\nОб этом можете не беспокоится.\nЯ думаю с этим вам всё понятно❗")


# Неизвестные команды
    else:
        bot.send_message(id,'❌ Неизвестная команда!\n\nВы отправили сообщение напрямую в чат бота, или структура меню была изменена Админом.\n\nℹ️ Не отправляйте прямых сообщений боту или обновите Меню, нажав на кнопку:    ➡️  /start')
        bot.send_message(message.chat.id, "😧")
 
                    
bot.polling(none_stop = True)