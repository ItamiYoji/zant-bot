import vk_api, random
import sqlite3

vk_session = vk = vk_api.VkApi(token='0a877d2e4a2493b01d06cec3e3e47bc48ffe069d4565d6b94915931ce69cac7f79e20fa9c546678152fde')

from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

conn = sqlite3.connect('summoners.db')
с = conn.cursor()

global Random

def random_id():
    return random.randint(0, 100000000)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:



            if event.text.lower() == 'начать' or event.text.lower() == 'привет' or event.text.lower() == 'здравствуйте':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Ты попал в Зантерию. Что это? Это мир, где только сильнейшие получают всё. Здесь мы проводим любительские турниры по LoL и TFT. Хочешь быть одним из нас? Если да, то пройди регистрацию (просто нажми на кнопку)',
                    keyboard = open ("registration.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'регистрация':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Чтобы подниматься на вершину ты должен зарегистрироваться, всё что нужно это вписать свой ник из лиги сюда: \nhttps://vk.com/topic-186161229_41270767 \n Окей, ты готов побеждать? Лучше всего это делать в компании. Смекаешь? \n*голос КАПИТАНА Джека Воробья*',
                    keyboard = open ("teams.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'понеслась':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Чтобы побеждать противников в компании хороших людей (то есть если хочешь вступить в команду), то напиши нашему глав. админу: (https://vk.com/goodzant)  \n Стать кэпом - основать свою команду \n FAQ - вопросы-ответы(наш админ в процессе его создания) \n Правила - перед законом все равны \n Zteam - стать частью организаторского состава) ',
                    keyboard = open ("normal.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'стать кэпом':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Хочешь стать командиром собственного корабля? Напиши тогда сюда: \nhttps://vk.com/goodzant',
                    keyboard = open ("normal.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'faq':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Что-то не понятно? Не бойся, всё есть здесь: (FAQ в разработке)',
                    keyboard = open ("normal.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'правила':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Законы нашего малого государства могут быть несовершенными, мы прислушиваемся к своим гражданам. Наше священное писание: https://vk.com/@zanteria-rules',
                    keyboard = open ("normal.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
            elif event.text.lower() == 'zteam':
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Хочешь стать частью нашей администрации? Пиши нашему глав. админу:\n Алексею (https://vk.com/goodzant) ',
                    keyboard = open ("normal.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )

            else:
                vk.messages.send(
                    user_id = event.user_id,
                    message = 'Я дико извиняюсь, но я не всего лишь бот, так что не понимаю всех слов. Давай начнём сначала(напишите "Начать" или нажмите кнопку) ',
                    keyboard = open ("start.json", 'r', encoding = "UTF-8").read(),
                    random_id = random_id()
                )
