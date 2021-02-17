'''
Задание 2
Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, чтобы она перехватывала исключения, когда переданы некорректные аргументы.
Первые два нужно приводить к вещественному числу при помощи float(), а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, если приведение типов не сработало.
'''

def discounted2(price , discount, max_discount=20):
    '''
    discounted2(price , discount, max_discount=20)
    при некооректно вводе даных функция вернет 'errore'
    '''
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        if max_discount >= 99:
            raise ValueError('Ошибка по сумме скидки')
        elif discount > max_discount:
            return price
        else: 
            return price -(price*discount/100)
    except (ValueError, TypeError):
        print('Случилась беда!!!!!!!')
        return 'errore'

print(discounted2('ssdsd',15,20))
print(discounted2('500',15,20.4))
print(discounted2('ssdsd',15,20))
print(discounted2('2500',15,20))

print('\n')
help(discounted2)