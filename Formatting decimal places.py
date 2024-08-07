def format_numbers(numbers):
    # Formatear cada número a dos decimales
    formatted_numbers = [f"{number:.2f}" for number in numbers]
    return formatted_numbers

# Ejemplo de uso
numbers = [3.14159, 2.71828, 1.61803, 0.57721]
formatted = format_numbers(numbers)
print("Números formateados:", formatted)
