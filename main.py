# ALGORITMOS Y ESTRUCTURAS DE DATOS - UAP
# Lista de Ejercicio 03 - Ejercicios Condicional y Iteración
# Nombre: Jared Peter
# Numero de alumno: 36046

# 1
numeros = int(input("Ingrese la cantidad de números que requiere: "))

a, b = 0, 1

final_string = ""

if numeros > 0:
    final_string += ">> 0 "
if numeros > 1:
    final_string += ">> 1 "

for i in range(2, numeros):
    a, b = b, a + b
    final_string += f">> {b} "

print(final_string)

# 2.
# Primer caso: if
# Segundo caso: match

# 3.

while True:
    lado_1 = (int)(input("Lado 1:"))
    lado_2 = (int)(input("Lado 2:"))
    lado_3 = (int)(input("Lado 3:"))

    if lado_1 != lado_2 != lado_3:
        print("Escaleno")
    elif lado_1 == lado_2 == lado_3:
        print("Equilatero")
    else:
        print("Isosceles")

    continuar = input("Presione enter para continuar o cualquier otra tecla para salir")
    if continuar.strip():
        break

# 4.

numero = (int)(input("Ingrese un numero: "))

i = 0
while (i <= numero):
    print(i)
    i += 1

for i in range(numero + 1):
    if (i % 2 == 0):
        print(i)

# 5.
def romano():
    numero = int(input("Ingrese un número entre 1 y 1000: "))

    romano = ""

    while numero > 0:
        if numero >= 1000:
            romano += "M"
            numero -= 1000
        elif numero >= 900:
            romano += "CM"
            numero -= 900
        elif numero >= 500:
            romano += "D"
            numero -= 500
        elif numero >= 400:
            romano += "CD"
            numero -= 400
        elif numero >= 100:
            romano += "C"
            numero -= 100
        elif numero >= 90:
            romano += "XC"
            numero -= 90
        elif numero >= 50:
            romano += "L"
            numero -= 50
        elif numero >= 40:
            romano += "XL"
            numero -= 40
        elif numero >= 10:
            romano += "X"
            numero -= 10
        elif numero >= 9:
            romano += "IX"
            numero -= 9
        elif numero >= 5:
            romano += "V"
            numero -= 5
        elif numero >= 4:
            romano += "IV"
            numero -= 4
        else:
            romano += "I"
            numero -= 1

    print(romano)


# 6.
letra = input("Ingrese una letra (A o P)")
calificacion_1 = (int)(input("Ingrese calificacion 1: "))
calificacion_2 = (int)(input("Ingrese calificacion 2: "))
calificacion_3 = (int)(input("Ingrese calificacion 3: "))

if str.upper(letra) == 'A':
    promedio = (calificacion_1 + calificacion_2 + calificacion_3)/3
    print(f"Promedio: {promedio}")
elif str.upper(letra) == 'P':
    promedio = ((calificacion_1 * 5) + (calificacion_2 * 3) + (calificacion_3 * 2))/(5 + 3 + 2)
    print(f"Promedio ponderado: {promedio}")

# 7

def dobleFactorial(numero):
    if (numero % 2 == 0):
        return "Numero no es impar"

    numero_final = 1

    while numero > 0:
        numero_final *= numero
        numero -= 2

    return numero_final

print(dobleFactorial(17))


# 8
def suma_de_numeros(numero):
    if not isinstance(numero, int) or not numero >= 0:
        return "Numero es invalido"

    num = 0
    for i in str(numero):
        i = int(i)
        num += i
    return num

# 9.
# Usando N = 533 --> DXXXIII
# Usando N = 970 --> CMLXX

# 10.
# Usando N = 23 --> 316234143225
# Usando N = 17 --> 34459425
