import ephem

def list_planets_get():
    list_turple_planet = ephem._libastro.builtin_planets() # получаем список всех планет и лун
    list_planets = [] # Создаем нащ список планет/пока пустой
    for planets in list_turple_planet:
        if planets[1] == 'Planet' and planets[2]!= 'Sun' and planets[2]!='Moon': # Забираем в наш список все планеты, исключая солнце и луну
            list_planets.append(planets[2])
    return list_planets

print(list_planets_get())


from datetime import date, datetime

today = date.today()
['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
print(today)
a =ephem.constellation(ephem.Pluto('2021/02/18'))
print(a)