import contador

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Debe ingresar un número mayor o igual a 0.")
        else:
            contador.cuenta_regresiva(numero)
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()