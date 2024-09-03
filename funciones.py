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



## ASIGNACION
# * toma todos los valores hasta el anteultimo (porque tiene que dejar lugar para i)
g, *h, i = (1, 2, 3, 4, 5, 6)

# Operador walrus
a = 0
if (a := 1) == 1:
    print('yea')
else:
    print('nop')



## FUNCIONES
# Subprograma o subrutina que forma parte de un algoritmo principal.
# Permite la reutilizacion de porciones de codigo y evita repetirse. Facilita el mantenimiento y testeo

def func():
    print("Hola")
    return [1, 2, 3]


## GLOBALES
# Una variable es global cuando puede ser accedidad desde cualquier parte del programa. Es local cuando solo puede ser accedida en el contexto en que fue definida
z = 12

def fun():
    # no lo cambia
    z = 33

def new_fun():
    # Si lo cambia
    global z
    z = 33

new_fun()
print(z)

## EXCEPCIONES
# Gestion de errores o problemas inesperados
# Por ej: division por 0, o acceso a variable no definida (null pointer)
# Es para no cerrar el programa inesperadamente ante un error

try:
    a = 5/0
except Exception as e:
    # Tambien se puede hacer otra cosa como cerrar la base de datos, u otra cosa
    # Nunca dejar vacio el except
    print(f'Error inesperado {e}')

try:
    raise Exception("Exception personalizada")
except Exception as e:
    print(f'Error inesperado {e}')
