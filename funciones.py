# Puntero: una variable que tiene como contenido una direccion a la memoria

a = ["uno", "dos"]
print(id(a))

b = a
print(id(a))

a[0] = "tres"
print(b)
# b tambien cambia, ya que tienen la misma direccion de memoria con b

x = a.copy()
# es una copia de a, apunta a otro espacio en la memoria
