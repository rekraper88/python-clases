from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Receta:
    titulo: str
    descripcion: str
    tiempo: int
    siguiente: Receta = None  

def agregar(receta: Receta):
    actual = root
    while actual.siguiente != None:
        actual = actual.siguiente
    actual.siguiente = receta

def agregar_al_principio(receta: Receta):
    global root
    receta.siguiente = root
    root = receta

def agregar_en_posicion(receta: Receta, posicion: int):
    actual = root
    i = 0

    while actual != None and i < posicion - 1:
        actual = actual.siguiente
        i += 1

    receta.siguiente = actual.siguiente
    actual.siguiente = receta


root = Receta('nose', 'asdasda', 14)
nueva_receta = Receta('asdas', 'dsdsdas', 14)
receta1 = Receta('fideos', 'asdasda', 13)
receta2 = Receta('tarta', 'no se', 13)

agregar_al_principio(receta1)
agregar(nueva_receta)
# agregar_en_posicion(receta2, 1)

actual = root
while actual != None:
    print(actual.titulo)
    actual = actual.siguiente
