lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def busqueda_lineal(lista, elemento):
    for elem in range(len(lista)):
        if lista[elem] == elemento:
            return lista[elem]

# def ordenar_lista(lista):
#     nueva_lista = []
#     for item in lista:
#         if item

def busqueda_binaria(lista, elemento):
    lista.sort()

    lista_restante = []
    list_half_element = len(lista) // 2

    if lista[list_half_element] > elemento:
        lista_restante = lista[0:list_half_element]
    elif lista[list_half_element] < elemento:
        lista_restante = lista[list_half_element:len(lista)]
    else:
        return elemento

    return busqueda_binaria(lista_restante, elemento)

print(busqueda_binaria(lista, 2))
