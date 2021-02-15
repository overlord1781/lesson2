'''
Практика: Сравнение строк
1. аписать функцию, которая принимает на вход две строки
2. Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
3. Если строки одинаковые, вернуть 1
4. Если строки разные и первая длиннее, вернуть 2
5. Если строки разные и вторая строка 'learn', возвращает 3
6. Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты
'''

def strings_compares(string1 , string2):
    if not isinstance(string1,str) or not isinstance(string2,str):
        return 0
    elif string1 == string2:
        return 1
    elif len(string1) > len(string2) and string1 != string2 and string2 != 'learn':
        return 2
    elif string1 != string2 and string2 == 'learn':
        return 3

print(strings_compares(1,'ssdsd')) # Передача цифр (не строк)
print(strings_compares('одинаковые строки','одинаковые строки')) # Одинаковые строки
print(strings_compares('длиная строка','короткая')) # Передача 1 строка длинее 2
print(strings_compares('длиная строка','learn')) # Передача 1 строка длинее 2 
print(strings_compares('длин','learn'))
print(strings_compares('короткая','длиная строка')) # Передача 1 строка длинее 2
print(strings_compares('learn','learn')) # Передача 1 строка длинее 2
