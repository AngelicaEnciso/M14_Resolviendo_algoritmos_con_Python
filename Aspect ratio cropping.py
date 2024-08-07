import math


def convert_to_16_9_resolution(x_res, y_res):
    # La relación de aspecto deseada es 16:9
    aspect_ratio = 16 / 9

    # Mantener la altura (y_res) igual y calcular el nuevo ancho (x_res_16_9)
    x_res_16_9 = math.ceil(y_res * aspect_ratio)

    return x_res_16_9, y_res


# Ejemplo de uso
x_res = 1440
y_res = 1080
new_x_res, new_y_res = convert_to_16_9_resolution(x_res, y_res)
print(f"Resolución con aspecto 16:9 que mantiene la altura igual: {new_x_res}x{new_y_res}")
