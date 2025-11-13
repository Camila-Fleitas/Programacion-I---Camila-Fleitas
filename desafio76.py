#**Desafío 76**
#Construye un árbol binario simple con al menos 3 niveles de profundidad. Cada nodo debe contener un número entero como valor. Una vez construido el árbol, 
#implementa una función que imprima los valores de los nodos siguiendo un recorrido en preorden.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def preorden(nodo):
    if nodo is None:
        return
    print(nodo.valor, end=" ")
    preorden(nodo.izquierdo)
    preorden(nodo.derecho)

raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)

raiz.izquierdo.izquierdo = Nodo(3)
raiz.izquierdo.derecho = Nodo(7)
raiz.derecho.izquierdo = Nodo(12)
raiz.derecho.derecho = Nodo(18)

# Agrego un nivel más en la rama izquierda
raiz.izquierdo.izquierdo.izquierdo = Nodo(2)

print("Recorrido en preorden:")
preorden(raiz)
