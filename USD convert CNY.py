def usd_to_cny(usd_amount):
    # Tipo de cambio fijo (puedes ajustar este valor según el tipo de cambio actual)
    exchange_rate = 7.00

    # Convertir USD a CNY
    cny_amount = usd_amount * exchange_rate

    # Formatear el resultado como una cadena
    result = f"{cny_amount:.2f} Chinese Yuan"

    return result


# Ejemplo de uso
usd_amount = 100
conversion_result = usd_to_cny(usd_amount)
print(conversion_result)
