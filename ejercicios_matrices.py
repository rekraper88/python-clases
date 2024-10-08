list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]

def encontrar_adyacente(list, x):
    for i in range(len(list)):
        if i != len(list):
            if list[i] + list[i + 1 % len(list)] == x:
                return "Existe"
            else:
                return -1
    return -1

print(encontrar_adyacente(list, 20))
        
