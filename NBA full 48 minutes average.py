def extrapolate_ppg(ppg, mpg):
    # Si mpg es 0, retornar 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Calcular la extrapolación de ppg para 48 minutos
    ppg_48 = (ppg / mpg) * 48

    # Redondear a la décima más cercana
    ppg_48_rounded = round(ppg_48, 1)

    return ppg_48_rounded


# Ejemplo de uso
ppg = 20  # Puntos por juego
mpg = 30  # Minutos jugados por juego

extrapolated_ppg = extrapolate_ppg(ppg, mpg)
print(f"Extrapolación de puntos por juego para 48 minutos: {extrapolated_ppg}")
