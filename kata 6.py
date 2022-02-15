




planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
print('Hay', len(planetas), 'planetas')

planetas.append('Pluton')
print(planetas[-1], 'es el ultimo planeta en la lista')

user_planet = input('Ingrese el nombre de un planeta comenzando con mayúscula')


planet_index = planetas.index(user_planet)


print('planetas mas cercanos a ' + user_planet)
print(planetaVenuss[0:planet_index])


print('planetas mas lejanos a' + user_planet)
print(planetas[planet_index + 1:])




