'''
Задание
Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

'''
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date
import ephem
import settings

logtime = '%(asctime)s %(message)s'
logdate = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(filename='bot.log', level=20, format=logtime, datefmt=logdate) #Логирование событий бота


PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSOWRD }}

#Функция для получения оригинального списка небесных тел из ephem

def list_planets_get():
    list_turple_planet = ephem._libastro.builtin_planets() # получаем список всех планет и лун
    list_planets = [] # Создаем нащ список планет/пока пустой
    for planets in list_turple_planet:
        if planets[1] == 'Planet' and planets[2]!= 'Sun' and planets[2]!='Moon': # Забираем в наш список все планеты, исключая солнце и луну
            list_planets.append(planets[2])
    return list_planets
['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
def answer_constellation(update , context):
    print('Вызван /planets')
    user_planet = update.message.text.split()[1]
    print(user_planet)
    today = date.today()

    if user_planet == 'Mercury':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Mercury(today))[1])}')
    elif user_planet == 'Venus':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Venus(today))[1])}')
    elif user_planet == 'Mars':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Mars(today))[1])}')
    elif user_planet == 'Jupiter':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Jupiter(today))[1])}')
    elif user_planet == 'Saturn':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Saturn(today))[1])}')
    elif user_planet == 'Uranus':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Uranus(today))[1])}')
    elif user_planet == 'Neptune':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Neptune(today))[1])}')
    elif user_planet == 'Pluto':
        update.message.reply_text(f'Сегодня {today} планета {user_planet} находится в созвездии {(ephem.constellation(ephem.Pluto(today))[1])}')
    


def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет пользователь! Ты вызвал команду СТРАТ')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
    
def main():
    PASS = settings.API_KEY
    mybot = Updater(PASS, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', answer_constellation))
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("бот запустился")

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()