def calculate_total_pressure(M1, M2, m1, m2, V, T):
    # Constante de los gases en dm^3⋅atm⋅K^−1⋅mol^−1
    R = 0.082

    # Convertir la temperatura de °C a K
    T_kelvin = T + 273.15

    # Calcular la presión total usando la fórmula dada
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V

    return P_total


# Ejemplo de uso
M1 = 32.0  # Masa molar del primer gas en g⋅mol^−1
M2 = 28.0  # Masa molar del segundo gas en g⋅mol^−1
m1 = 10.0  # Masa del primer gas en gramos
m2 = 15.0  # Masa del segundo gas en gramos
V = 5.0  # Volumen del recipiente en dm^3
T = 25.0  # Temperatura en °C

# Calcular la presión total
pressure = calculate_total_pressure(M1, M2, m1, m2, V, T)
print(f"La presión total ejercida por los gases es: {pressure:.2f} atm")
