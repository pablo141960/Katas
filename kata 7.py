


new_planet = ''
planets = []


while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('ingrese el nombre del planeta\n')
for planet in planets:
    print(planet)