# Ejercicio 1.1
print("Ejercicio 1.1")
def potencia():
    print("Calcularanse potencia de dous números")
    n1 = input("Ingrese un número enteiro: ")
    n2 = input("Ingrese otro número enteiro: ")

    for x in range(int(n1), int(n2)):
        print(x * x)

    print("É todo por agora")


potencia()

# Ejercicio 1.2

# Ejercicio 1.3

# Ejercicio 1.4

# Ejercicio 1.5

# Ejercicio 6.1
print("Ejercicio 6.1")
def imprimir_dos_primeros(caracteres):
    print(caracteres[:2])

def imprimir_tres_ultimos(caracteres):
    print(caracteres[-3:])

def imprimir_cada_dos(caracteres):
    print(caracteres[::2])

def imprimir_inverso(caracteres):
    print(caracteres[::-1])

def imprimir_en_senso_inverso(caracteres):
    print(caracteres + caracteres[::-1])

# Ejemplos de uso
cadena = "reflexo"
imprimir_dos_primeros(cadena)
imprimir_tres_ultimos(cadena)
imprimir_cada_dos(cadena)
imprimir_inverso(cadena)
imprimir_en_senso_inverso(cadena)

# Ejercicio 6.2
print("Ejercicio 6.2")
def insertar_entre_letras(cadena, caracter):
    resultado = caracter.join(cadena)
    print(resultado)

def reemplazar_espacios(cadena, caracter):
    resultado = cadena.replace(' ', caracter)
    print(resultado)

def reemplazar_digitos(cadena, caracter):
    resultado = ''.join(caracter if c.isdigit() else c for c in cadena)
    print(resultado)

def insertar_cada_tres_digitos(cadena, caracter):
    grupos = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
    resultado = caracter.join(grupos)
    print(resultado)

# Ejemplos de uso
cadena1 = "separar"
caracter1 = ","
insertar_entre_letras(cadena1, caracter1)

cadena2 = "meu arquivo de texto.txt"
caracter2 = "_"
reemplazar_espacios(cadena2, caracter2)

cadena3 = "Súa clave é: 1540 e 'X'"
caracter3 = "X"
reemplazar_digitos(cadena3, caracter3)

cadena4 = "2552552550"
caracter4 = "."
insertar_cada_tres_digitos(cadena4, caracter4)

# Ejercicio 7.1
print("Ejercicio 7.1")
def menorAmayor(tupla):
    ordenada = True
    numElementos = len(tupla)
    if numElementos <= 1:
        ordenada = True
    else:
        for i in range(len(tupla)):
            if i + 1 < numElementos:
                if tupla[i] > tupla[i + 1]:
                    ordenada = False
                    break
            else:
                break
    return ordenada


print(menorAmayor((1, 2, 3, 4, 5)))

# Ejercicio 7.2.1
print("Ejercicio 7.2.1")
def coincidenFichas(ficha1, ficha2):
    """
    Función que comprueba si dos fichas de dominó son combinables.

    La función compara los lados de las fichas entre si y devuelve un True si combinan,
    si no hay coincidencia numérica entre los lados devuelve False.

    :param ficha1: Tuple
    :param ficha2: Tuple
    :return: boolean
    """
    if ficha1[0] == ficha2[0]:
        return True
    elif ficha1[0] == ficha2[1]:
        return True
    elif ficha1[1] == ficha2[0]:
        return True
    elif ficha1[1] == ficha2[1]:
        return True
    else:
        return False

ficha1= (3, 4)
ficha2= (5, 4)

if coincidenFichas(ficha1,ficha2):
    print("Las fichas coinciden")
else:
    print("Las fichas no coinciden")

# Ejercicio 7.2.2
print("Ejercicio 7.2.2")
def coincidenFichasCadena(ficha):
    """
    Función que comprueba si dos fichas de dominó son combinables.

    La función compara los lados de las fichas entre si y devuelve un True si combinan,
    si no hay coincidencia numérica entre los lados devuelve False.

    :param ficha: String
    :return: boolean
    """
    fichas=ficha.split()
    ficha1=fichas[0].split("-")
    ficha2=fichas[1].split("-")

    return coincidenFichas(ficha1,ficha2)

print(coincidenFichasCadena("3-4 2-5"))

# Ejercicio 7.5.1
print("Ejercicio 7.5.1")
def numerosPrimos(lista):
    lista=[1,2,3,4,5,6,7,8,9,10]
    for numero in lista:
        if numero//numero &  numero//1:
            print("El numero "+numero+" es primo")
        else:
            print("El número "+numero+" no es primo")
