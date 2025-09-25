#Crea una función que reciba una lista y un entero n, y devuelva los n primeros elementos.

#--------------------------------------------------------------------------------------------

# Definimos una función que recibe una lista y un número entero n
def primeros_elementos(lista, n):
    # Usamos slicing [:n] para obtener los n primeros elementos
    return lista[:n]

# Ejemplo de uso:
mi_lista = [10, 20, 30, 40, 50]

# Queremos los 3 primeros elementos
resultado = primeros_elementos(mi_lista, 3)

print(resultado)  # Salida: [10, 20, 30]