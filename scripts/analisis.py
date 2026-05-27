#Lista de equipos de futbol participantes
equipos= ["Boca Juniors", "River Plate", "Racing", "Independiente"]

#Cantidad de partidos ganados por equipo
victorias= [5, 4, 3, 2]

#Equipo con mayor rendimiento
max_victorias = max (victorias)
mejor_equipo = equipos[victorias.index(max_victorias)]

print("Equipo con mejor rendimiento:", mejor_equipo)
print("Cantidad de partidos ganados:", max_victorias)
