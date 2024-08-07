def calculate_pet_ages(humanYears):
    if humanYears < 1 or not isinstance(humanYears, int):
        raise ValueError("humanYears debe ser un número entero mayor o igual a 1")

    # Inicializar los años de gato y perro
    catYears = 0
    dogYears = 0

    # Calcular los años de gato
    if humanYears == 1:
        catYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4

    # Calcular los años de perro
    if humanYears == 1:
        dogYears = 15
    elif humanYears == 2:
        dogYears = 15 + 9
    else:
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Solicitar al usuario que ingrese los años humanos
try:
    humanYears = int(input("Ingrese los años humanos: "))
    ages = calculate_pet_ages(humanYears)
    print(f"Años humanos: {ages[0]}, Años de gato: {ages[1]}, Años de perro: {ages[2]}")
except ValueError:
    print("Por favor, ingrese un número entero válido mayor o igual a 1.")
