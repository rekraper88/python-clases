import json


def create_file(content):
    with open("curso_con_bono_aumentado.csv", "w") as file:
        file.write(content)


lista_lineas = []

# poner encoding='utf-8' si no anda en windows
with open("curso.csv", "r") as file:
    while (line := file.readline().strip()):
        line = line.split('|')
        line[3] = int(line[3]) * 1.13
        lista_lineas.append(line)

with open("curso_con_bono_aumentado.csv", "w") as file:
    for line in lista_lineas:
        file.write(f"{line[0]}|{line[1]}|{line[2]}|{line[3]}")
