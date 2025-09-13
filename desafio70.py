# -----------------------------------------------
# Definición de una excepción personalizada
# -----------------------------------------------

# Creamos una nueva clase de excepción llamada NegativeNumberError.
# Hereda de la clase base 'Exception', lo que significa que
# podemos tratarla como cualquier otra excepción en Python.
class NegativeNumberError(Exception):
    pass  # 'pass' indica que no agregamos nada más a la clase (es mínima).


# -----------------------------------------------
# Importación de librerías
# -----------------------------------------------

import math  # Usaremos la función sqrt() para calcular raíces cuadradas.


# -----------------------------------------------
# Programa principal con manejo de errores
# -----------------------------------------------

try:
    # Pedimos al usuario que ingrese un número (puede ser decimal).
    # La función input() devuelve texto, por lo que usamos float()
    # para convertirlo a número con decimales.
    num = float(input("Ingrese un número para calcular su raíz cuadrada: "))

    # Verificamos si el número ingresado es negativo.
    if num < 0:
        # Si es negativo, disparamos (raise) la excepción personalizada
        # que creamos antes: NegativeNumberError.
        # Pasamos un mensaje explicativo que luego podrá mostrarse.
        raise NegativeNumberError("No se puede calcular la raíz cuadrada de un número negativo.")

    # Si el número es válido (no es negativo),
    # usamos math.sqrt() para calcular su raíz cuadrada.
    resultado = math.sqrt(num)

    # Mostramos el resultado al usuario.
    print(f"La raíz cuadrada de {num} es: {resultado}")


# -----------------------------------------------
# Bloques de manejo de excepciones
# -----------------------------------------------

# Si ocurre nuestra excepción personalizada (número negativo):
except NegativeNumberError as e:
    # Se imprime el mensaje que pasamos al lanzar la excepción.
    print("Error:", e)

# Si ocurre un ValueError (por ejemplo, el usuario escribe letras
# en vez de números), se captura aquí:
except ValueError:
    print("Error: Debe ingresar un número válido.")