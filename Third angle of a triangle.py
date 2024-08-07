def third_angle_of_triangle(angle1, angle2):
    # Verificar que los ángulos proporcionados sean válidos
    if not (0 < angle1 < 180 and 0 < angle2 < 180):
        raise ValueError("Los ángulos deben ser mayores que 0 y menores que 180 grados.")
    if angle1 + angle2 >= 180:
        raise ValueError("La suma de los dos ángulos no puede ser mayor o igual a 180 grados.")

    # Calcular el tercer ángulo
    angle3 = 180 - (angle1 + angle2)

    return angle3


# Ejemplo de uso
angle1 = 50
angle2 = 60
third_angle = third_angle_of_triangle(angle1, angle2)
print(f"El tercer ángulo del triángulo es: {third_angle} grados")
