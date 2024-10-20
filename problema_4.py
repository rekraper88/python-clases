from __future__ import annotations
from dataclasses import dataclass, field

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

# loop([root])

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
def loop(nodos):
    if not nodos: return

    n = []
    for nodo in nodos:
        if nodo:
            print(nodo.valor)
            n.extend([nodo.left, nodo.right])

    loop(n)

loop([root])

