import math


def age_range(age):
    if age <= 14:
        # Usar la fórmula alternativa para edades 14 o menores
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Usar la fórmula clásica para edades mayores a 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)

    return [min_age, max_age]


# Ejemplo de uso
age = 25
range_age = age_range(age)
print(f"Rango de edad para {age} años: {range_age[0]}-{range_age[1]}")
