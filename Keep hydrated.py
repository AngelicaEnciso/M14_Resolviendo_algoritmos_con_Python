import math


def water_needed(hours):
    # Cantidad de agua que Nathan bebe por hora
    water_per_hour = 0.5

    # Calcular el total de agua necesario
    total_water = hours * water_per_hour

    # Redondear hacia abajo al entero más cercano
    liters_needed = math.floor(total_water)

    return liters_needed


# Lista de tiempos de ciclismo en horas
cycling_hours_list = [3.5, 4.7, 6.2, 8.1, 10.0]

# Calcular y mostrar la cantidad de agua necesaria para cada tiempo
for hours in cycling_hours_list:
    liters = water_needed(hours)
    print(f"Para {hours} horas de ciclismo, Nathan necesitará beber {liters} litros de agua.")
