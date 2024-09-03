import copy
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
# .copy() copia solamente el primer nivel del array
print(x)










x = [[1, 2, 3], ['Juan', 'Ana'], True]
y = x.copy()

# Cada array dentro del array es referencia a otro espacio en la memoria,
# asi que cuando cambie un elemento de un sub-array del elemento padre,
# la variable que es una copia tambien va a cambiar, ya que contiene
# una referencia externa (esta referencia es la que cambio)
x[0][1] = 333

# deepcopy copia todos los niveles, asi que no importa si cambia un sub elemento
# en el array que fue copiado, el array que es copia no va a cambiar
z = copy.deepcopy(x)


print(x)
print(y)
