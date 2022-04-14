import telebot

bot = telebot.TeleBot('5247858620:AAGE8oocfqDOX_Bq-8VHEz0_4GMIMMgVdTU')
groupid = '-1001731474532'

user_dict = {}
user_chats = 0

class User:
    def __init__(self):
        self.fio = ''
        self.otz = ''
        self.phone = ''
    def setFIO(self, s_fio):
        self.fio = s_fio

    def setOtz(self, s_otz):
        self.otz = s_otz

    def setPhone(self, s_phone):
        self.phone = s_phone

@bot.message_handler(commands=['start'])
def send_welcome1(message):
    global user
    chat_id = message.chat.id
    user_dict[chat_id] = user
    msg = bot.send_message(chat_id,
                           "Барабанный привет! \nНа связи НЕ ШКОЛА БАРАБАНОВ🥁 \nДавайте знакомиться, меня зовут Аня, а вас?")
    bot.register_next_step_handler(msg, process_fio_step)

def process_fio_step(message):
    global user
    try:
        chat_id = message.chat.id
        user.setFIO(message.text)
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, 'Приятно познакомиться! \nРасскажите, что ждёте от пробного урока??? ')
        bot.register_next_step_handler(msg, process_otz_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')



def process_otz_step(message):
    global user
    try:
        chat_id = message.chat.id
        user.setOtz(message.text)
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, 'Супер! Нам осталось выбрать время вашего урока🥁🔥 \nДля этого напишите пожалуйста ваш номер телефона и в ближайшее время я с Вами свяжусь🙌🏼☎️')
        bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_phone_step(message):
    global user
    try:
        chat_id = message.chat.id
        user.setPhone(message.text)
        user_dict[chat_id] = user
        bot.send_message(message.from_user.id, f'ФИО: {user.fio} \n'
                 + f'Чего ждёте от урока: {user.otz} \n'
                 + f'Номер телефона: {user.phone} \n')
    except Exception as e:
        bot.reply_to(message, 'oooops')
        print(e)
    send_to_group()




def send_to_group():
    global groupid, user
    try:
        bot.send_message(groupid, 'НОВАЯ ЗАЯВКА!' + '\n'
                     + f'ФИО: {user.fio} \n'
                     + f'Номер  телефона: {user.phone} \n'
                     + f'Ожидание от урока: {user.otz} \n')
    except Exception as e:
        print(e)

user = User()

bot.polling()
