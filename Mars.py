
import ephem


spisok_planet = ephem._libastro.builtin_planets()
for planets in spisok_planet:
    print(planets[2])