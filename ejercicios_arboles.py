from __future__ import annotations
from dataclasses import dataclass, field
from random import randint

# @dataclass
# class Persona:
#     numero: int = 0
#     hombre: bool = True
#     # hijos: list = field(default_factory=list)
#     next: Persona = None

# root = Persona(1, True)

# def agregar(nueva_persona: Persona):
#     actual = root
#     while actual.next != None:
#         actual = actual.next
#     actual.next = nueva_persona


# agregar(Persona(2, False))
# def imprimir():
#     actual = root
#     while actual != None:
#         print(actual.numero)
#         actual = actual.next

# imprimir() 

# # root.hijos.append(Persona(1, True))
# # root.hijos.append(Persona(2, False))
# # root.hijos.append(Persona(3, True))

@dataclass
class Node:
    numero: int = 0
    next: Node = None


prim = Node(1)
prim.next = Node(7)


sec = Node(3)
sec.next = Node(4)
sec.next.next = Node(8)

def concatenar(prim, sec):
    ultimo_prim = prim

    while ultimo_prim.next != None:
        ultimo_prim = ultimo_prim.next

    ultimo_prim.next = sec
    pint(prim)



def concatenar_ordenadamente(prim, sec):
    ultimo_prim = prim

    while ultimo_prim.next != None:
        ultimo_prim = ultimo_prim.next

    ultimo_prim.next = sec
    pint(prim)
