'''
Задание 1
Напишите функцию hello_user(), которая с помощью функции input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
'''

def hello_user():
    while True:
        a = input('Как дела ')
        if a == 'Хорошо':
            break

hello_user()