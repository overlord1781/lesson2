'''
Оценки
Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
Посчитать и вывести средний балл по всей школе.
Посчитать и вывести средний балл по каждому классу.
'''

all_marks = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
            {'school_class': '4б', 'scores': [3,2,2,5,2]}, 
            {'school_class': '4в', 'scores': [5,5,5,5,2]},]
mid_scores_scholl = 0
mid_scores_class = 0
for mid_scores in all_marks:
    mid_scores_scholl += sum(mid_scores['scores'])/len(mid_scores['scores']) # Расчет среднего бала по школе
    mid_scores_class = sum(mid_scores['scores'])/len(mid_scores['scores'])  # Расчет среднего бала по каждому классу
    print(f'Средний бал класса {mid_scores["school_class"]} составялет {mid_scores_class}')

print(f'Средний бал по школе составляет {mid_scores_scholl/len(all_marks)}')
