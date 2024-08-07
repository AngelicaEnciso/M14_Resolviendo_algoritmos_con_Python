def total_cost_of_mangoes(quantity, price_per_mango):
    # Calcular cuántos grupos de 3 mangos hay
    groups_of_three = quantity // 3

    # Calcular el número de mangos que se pagan
    paid_mangos = groups_of_three * 2 + (quantity % 3)

    # Calcular el costo total
    total_cost = paid_mangos * price_per_mango

    return total_cost


# Ejemplo de uso
quantity = 10
price_per_mango = 3
cost = total_cost_of_mangoes(quantity, price_per_mango)
print(f"El costo total de {quantity} mangos a {price_per_mango} por mango es: {cost}")
