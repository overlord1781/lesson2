'''
Задание 1
Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" и завершала работу при помощи оператора break
'''
def hello_user():
    try:
        while True:
            a = input('Как дела ')
            if a == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('\n был нажат ctrl+c')

hello_user()