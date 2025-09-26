# Desafío 2: Calculadora Simple: Escriba un programa que pida al usuario que ingrese dos números y luego 
# imprima la suma, la resta, la multiplicación y la división de esos números.

# Pedimos dos números al usuario y los convertimos a float
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Operaciones
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Resultados
print(f"Resultado suma: {suma}, Resultado resta: {resta}, Resultado multiplicación: {multiplicacion} y Resultado división: {division}")
