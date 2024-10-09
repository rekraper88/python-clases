# Lista localidades

import json

#with open("localidades.json", "r", encoding="UTF-8") as file:
#    data = json.load(file)

#    with open("localidades_cordoba.txt", "w") as file:
#        for localidad in data["localidades"]:
#            if localidad["provincia"]["id"] == "14":
#                file.write(localidad["nombre"] + "\n")

bonos_menor = []
bonos_mayor = []

with open("curso.csv", "r") as file:
    while line := file.readline().strip():
        bono = line.split("|")[3]
        if int(bono) <= 10000:
            bonos_menor.append(line)
        else:
            bonos_mayor.append(line)

with open("bonos_menor_10000.csv", "w") as file:
    for line in bonos_menor:
        file.write(line + '\n')

with open("bonos_mayor_10000.csv", "w") as file:
    for line in bonos_mayor:
        file.write(line + '\n')
