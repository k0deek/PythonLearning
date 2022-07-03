import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def get_token():
    return ""

def login_group():
    return vk_api.VkApi(token=get_token())

def get_longpoll(session):
    return VkBotLongPoll(session, group_id=)


session = login_group()

longpoll = get_longpoll(session)

getting_api = session.get_api()

def write_message(chat_id, message):
    session.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id': 0})

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


lock_numbers = False

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get(
            'text') != "" and event.from_chat:

        reseived_message_big = event.message.get('text')
        reseived_message = reseived_message_big.lower()

        if reseived_message == "хай":
            write_message(event.chat_id, "Хай)")
        elif reseived_message == "пока":
            write_message(event.chat_id, "Пока((")
        elif reseived_message == "старт":
            write_message(event.chat_id, "Ну что, наяривай!\n Для окончания напишите <Конец>")
            lock_numbers = True
        elif reseived_message == "конец":
            write_message(event.chat_id, "Натыкался, да?\n Для начала напишите <Старт>")
            lock_numbers = False
        elif lock_numbers == 1 and is_number(reseived_message):
            write_message(event.chat_id, int(reseived_message)+1)
        if reseived_message.find('какой') != -1:
            write_message(event.chat_id, "Какой")
        if reseived_message.find('какая') != -1:
            write_message(event.chat_id, "Какая")
        if reseived_message.find('какие') != -1:
            write_message(event.chat_id, "Какие")
        if reseived_message.find('какое') != -1:
            write_message(event.chat_id, "Какое")
        if reseived_message.find('что') != -1:
            write_message(event.chat_id, "Что")
        if reseived_message.find('кто') != -1:
            write_message(event.chat_id, "Кто")
        if reseived_message.find('который') != -1:
            write_message(event.chat_id, "Который")
        if reseived_message.find('которая') != -1:
            write_message(event.chat_id, "Которая")
        if reseived_message.find('которые') != -1:
            write_message(event.chat_id, "Которые")
        if reseived_message.find('которое') != -1:
            write_message(event.chat_id, "Которое")
        if reseived_message.find('где') != -1:
            write_message(event.chat_id, "Где")
        if reseived_message.find('когда') != -1:
            write_message(event.chat_id, "Когда")
        if reseived_message.find('почему') != -1:
            write_message(event.chat_id, "Почему")
        if reseived_message.find('зачем') != -1:
            write_message(event.chat_id, "Зачем")
        if reseived_message.find('откуда') != -1:
            write_message(event.chat_id, "Откуда")
        if reseived_message.find('сколько') != -1:
            write_message(event.chat_id, "Сколько")
        if reseived_message.find('чей') != -1:
            write_message(event.chat_id, "Чей")
        if reseived_message.find('чья') != -1:
            write_message(event.chat_id, "Чья")
        if reseived_message.find('чьи') != -1:
            write_message(event.chat_id, "Чьи")
        if reseived_message.find('чьё') != -1:
            write_message(event.chat_id, "Чьё")
