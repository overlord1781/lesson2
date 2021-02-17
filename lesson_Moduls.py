from collections import Counter

phones = ['Iphone', 'Samsung', 'LG','Iphone','Iphone','Iphone' ]

count = Counter(phones)

print(count['Iphone'])

text = 'Абра кадабра бумс!!!'

text_c = Counter(text.lower().replace(' ',''))

print(text_c)