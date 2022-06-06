import telebot
from telebot import types
import time
bot = telebot.TeleBot('5401142349:AAEu-dPJiYCRRIxamWSfLiO8OItzjbeN3bw')
count1 = 0
count2 = 0
f = open('script.txt', 'r')
quest = f.read().split('\n')
f.close()
@bot.message_handler(commands=['start'])
def start(m, res=False):
    name = m.from_user.first_name
    ans = f'Добро пожаловать в игру, {name}'
    bot.send_message(m.from_user.id, ans)
    bot.send_message(m.chat.id, 'Итак, главный герой оказался ночью в морге. Спросите, как так вышло?')
    bot.send_message(m.chat.id, 'Давайте узнаем, о чем он думал, когда очутился в столь щепетильной ситуации.')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    msg = bot.reply_to(m, 'Нажми: \nНАчать и погрузись в захватывающую историю', reply_markup=markup)
    bot.register_next_step_handler(m, start_2)
    # ожидания ввода от пользователя с переходом на другой шаг

def start_2(message):
    global vopros
    if message.text.strip() == 'Начать':
        for i in range (14):
            vopros = quest[i]
            msg = bot.send_message(message.chat.id, vopros.format(message.text))
            time.sleep(12)

    # bot.register_next_step_handler(message, start_4)
    # ожидания ввода от пользователя с переходом на другой шаг
# def start_4(message):
#     global vopros
#     global count1
#     global count2
#     for n in range (13):
#         if message.text.strip() == 'Продолжить':
#             count1 +=2
#         for i in range(1,14):
#             if count1 > count2:
#                 vopros = quest[i]
#                 msg = bot.send_message(message.chat.id, vopros.format(message.text))
#                 count2 +=1


bot.polling(none_stop=True, interval=0)
