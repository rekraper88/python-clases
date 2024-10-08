import json


def create_file(content):
    with open("curso_con_bono_aumentado.csv", "w") as file:
        file.write(content)


with open("curso.csv", "r") as file:
    while (line := file.readline().strip()):
        line = line.split('|')
        line[3]  = int(line[3]) * 1.13
        print(line)
