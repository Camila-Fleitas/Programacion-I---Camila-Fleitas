# Desafío:
# Solicita al usuario dos números enteros e implementa un try-except
# que maneje la división por cero y los valores no numéricos.
# Muestra mensajes de error apropiados en cada caso.

# --- Inicialización de variables ---
primer_numero = 0
segundo_numero = 0

# --- Bloque try-except para manejar errores ---
try:
    # Pedimos al usuario el primer número
    print("Ingrese el primer número:")
    primer_numero = int(input())  # Convertimos a entero

    # Pedimos al usuario el segundo número
    print("Ingrese el segundo número:")
    segundo_numero = int(input())  # Convertimos a entero

    # Intentamos realizar la división
    resultado = primer_numero / segundo_numero
    print("El valor resultante es:", resultado)

# Manejo del error de división por cero
except ZeroDivisionError:
    print("No se puede dividir por 0.")

# Manejo del error cuando el usuario ingresa un valor no numérico
except ValueError:
    print("Error: debe ingresar números enteros.")