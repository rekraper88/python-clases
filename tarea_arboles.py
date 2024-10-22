from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class NumberNode:
    valor: int = 0
    left: NumberNode = None
    right: NumberNode = None

# Building the tree based on the image
raiz = NumberNode(8)

raiz.left = NumberNode(9)
raiz.right = NumberNode(5)

raiz.left.left = NumberNode(11)
raiz.left.right = NumberNode(7)

raiz.right.left = NumberNode(6)
raiz.right.right = NumberNode(12)

raiz.left.left.left = NumberNode(15)
raiz.left.left.right = NumberNode(20)

raiz.left.right.left = NumberNode(3)
raiz.left.right.right = NumberNode(1)

raiz.left.left.left.left = NumberNode(19)
raiz.left.left.right.right = NumberNode(21)

raiz.left.right.left.right = NumberNode(2)

raiz.right.left.left = NumberNode(4)
raiz.right.left.right = NumberNode(14)

raiz.right.left.left.left = NumberNode(13)
raiz.right.left.right.right = NumberNode(10)

raiz.right.right.left = NumberNode(17)
raiz.right.right.right = NumberNode(18)

raiz.right.right.left.right = NumberNode(16)

def preorden(nodo):
    if nodo == None: return
    print(nodo.valor)
    preorden(nodo.left)
    preorden(nodo.right)

def inorden(nodo):
    if nodo == None: return
    inorden(nodo.left)
    print(nodo.valor)
    inorden(nodo.right)

def postorden(nodo):
    if nodo == None: return
    postorden(nodo.left)
    postorden(nodo.right)
    print(nodo.valor)



@dataclass
class Node:
    valor: str = ""
    father: Node = None
    left: Node = None
    right: Node = None

root = Node("a")
root.left = Node("b")
root.left.father = root
root.right = Node("c")
root.right.father = root

root.left.right = Node("d")
root.left.right.father = root.left

root.left.right.left = Node("g")
root.left.right.left.father = root.left.right
root.left.right.right = Node("h")
root.left.right.right.father = root.left.right

root.left.right.right.left = Node("j")
root.left.right.right.left.father = root.left.right.right

root.right.left = Node("e")
root.right.left.father = root.right
root.right.right = Node("f")
root.right.right.father = root.right


root.right.left.left = Node("i")
root.right.left.left.father = root.right.left
root.right.left.left.left = Node("k")
root.right.left.left.left.father = root.right.left.left

# 3. 
def preorden(arbol):
    if arbol == None: return
    print(arbol.valor)
    preorden(arbol.left)
    preorden(arbol.right)

def inorden(arbol):
    if arbol == None: return
    inorden(arbol.left)
    print(arbol.valor)
    inorden(arbol.right)

def postorden(arbol):
    if arbol == None: return
    postorden(arbol.left)
    postorden(arbol.right)
    print(arbol.valor)

# 4.
def loop(nodos):
    if not nodos: return

    n = []
    for nodo in nodos:
        if nodo:
            print(nodo.valor)
            n.extend([nodo.left, nodo.right])

    loop(n)


#5. 
#a
def nodo_interno(nodo):
    if nodo.left or nodo.right:
        return True
    else:
        return False

# c.
def encontrar_nivel(nodo):
    actual = nodo
    count = 0
    while actual != None:
        count += 1
        actual = actual.father
    return count

# print(encontrar_nivel(root.left.right.left))

# d.
def encontrar_altura(nodo):
    if nodo == None: return 0

    altura_izq = encontrar_altura(nodo.left)
    altura_der = encontrar_altura(nodo.right)

    return 1 + max(altura_izq, altura_der)

# e.
def encontrar_altura_raiz(raiz):
    # verificar si es raiz o no:
    if raiz.father != None: return "No es raiz"
    
    if raiz == None: return 0

    altura_izq = encontrar_altura(raiz.left)
    altura_der = encontrar_altura(raiz.right)

    return 1 + max(altura_izq, altura_der)

# f.
def encontrar_profundidad(nodo):
    actual = nodo
    count = -1
    while actual != None:
        count += 1
        actual = actual.father
    return count

# g.
def encontrar_rama(raiz, nodo):
    camino = []
    actual = nodo

    while actual != raiz:
        camino.append(actual.valor)
        actual = actual.father

    camino.append(raiz.valor)
    return " -> ".join(reversed(camino)) 

# print(encontrar_rama(root, root.left.right))


# 6.
def mostrar_como_arbol(nodos):
    if not nodos: return                                
    n = []
    for i, nodo in enumerate(nodos):
        if nodo:
            print(nodo.valor, end=" ")
            n.extend([nodo.left, nodo.right])
    print()
    mostrar_como_arbol(n)
    
    print(encontrar_altura(nodos[0]))

# mostrar_como_arbol([root])

# 7
class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return self.valor
        
#crea la arbol del ejercicio 7
raiz = Node("B")
raiz.left = Node("U")
raiz.left.left = Node("E")
raiz.left.right = Node("R")
raiz.left.right.right  = Node("R")
raiz.left.right.right.left = Node("A")
raiz.left.right.right.right = Node("O")
raiz.left.right.right.right.left = Node("S")

raiz.left.left.left = Node("N")
raiz.left.left.left.left = Node("O")
raiz.left.left.left.right = Node("A")
raiz.left.left.left.right.right = Node("S")

raiz.right = Node("I")
raiz.right.right = Node("L")
raiz.right.left = Node("E")
raiz.right.left.left = Node("N")

raiz.right.right.left = Node("B")
raiz.right.right.left.left = Node("A")
raiz.right.right.left.left.left = Node("O")


def obtener_palabras(nodo, palabra_actual="", palabras=[]):
    if nodo is None:
        return

    # Concatenamos el valor del nodo actual a la palabra
    palabra_actual += nodo.valor

    # Si es una hoja o no tiene más hijos isgnificativos, guardamos la palabra
    if nodo.left is None and nodo.right is None:
        palabras.append(palabra_actual)

    # Recorrer subárbol izquierdo y derecho
    obtener_palabras(nodo.left, palabra_actual, palabras)
    obtener_palabras(nodo.right, palabra_actual, palabras)

    return palabras

# palabras = obtener_palabras(raiz)
# print("Palabras obtenidas:", palabras)

