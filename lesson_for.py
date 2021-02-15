##################################################        FOR       ################################################## 
for number in range (3):
    print(f'Привет мир {number}!')

print('\n')
##################################################        for работа со строкой       ################################################## 
for letter in 'python':
    print(letter.upper())
print('\n')
##################################################        for разбивка строки на слова       ################################################## 
string = 'Я хочу выучить питон'
for word in string.split():
    print(f'Длина слова {word} равна {len(word)}')
print('\n')
##################################################        for обход списка подсчет среднего V1      ################################################## 
spisok1 = [1 , 2 , 4 , 5 , 880]
summ = 0
for item in spisok1:
    summ += item
midle = summ/len(spisok1)
print(midle)
print('\n')
##################################################        подсчет среднего без for V2      ################################################## 
spisok1 = [1 , 2 , 4 , 5 , 880]
print(f'средний бал равен {sum(spisok1)/len(spisok1)}')
print('\n')
##################################################        for работа со списком словарей      ################################################## 
from lesson_if import discounted2

stock = [
		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1,
                'discount': 25},
		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
                'discount': 10},
		{'name': '', 'stock': 18, 'price': 10000.0, 
                'discount': 10}
]

for phone in stock:
    phone['finale_price'] = discounted2(phone['price'],phone['discount'], name=phone['name'] )
print(stock)