def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
x = int(input("Ingrese un número entero: "))
if es_par(x):
    print("El número es par")
else:
    print("El número es impar")

