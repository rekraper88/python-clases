from __future__ import annotations
from dataclasses import dataclass, field

# @dataclass
# class Node:
#     valor; str = ""
#     subnodes: list = field(default_factory=list)

@dataclass
class Node:
    valor: int = ""
    next: Node = None

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

root.next = node1
node1.next = node2
node2.next = node3

def imprimir_cantidad():
    actual = root
    cantidad = 0
    while actual != None:
        print(actual.valor)
        cantidad += 1
        actual = actual.next
    print(f"\n{cantidad}")

def buscar(numero):
    actual = root
    while actual != None:
        if actual.valor == numero:
            return True
        actual = actual.next
    return False

print(buscar(5))
imprimir_cantidad()