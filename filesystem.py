# Para abrir archivo: open(filepath, mode, encoding, errors, newline)


import json

contents = {"aa": 12, "bb": 21}

with open("myfile.txt", "w") as file:
    file.write(str(contents))


with open("busqueda.py", "r") as file:
    contents = file.readline()
print(contents)

with open("busqueda.py", "r") as file:
    contents = json.load(file)
print(contents)

