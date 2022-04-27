import numpy
import math
from FromMatric import *


# RESOLUCION DE MATRICES
# ---------------------
def productoMatriz():
    "Producto de dos matrices"
    print("Imprime la primera matriz:")
    filas1 = int(input("Limite: "))
    matriz1 = []
    for _ in range(filas1):
        matriz1.append(list(map(float, input().split())))

    print("Imprime la segunda matriz:")
    filas2 = int(input("Limite: "))
    matriz2 = []
    for _ in range(filas2):
        matriz2.append(list(map(float, input().split())))

    matriz_final = productoMatriz_re(matriz1, matriz2)
    print("Producto cruz:")
    print(numpy.array(matriz_final))


def Multipl_VFile_VColum():
    "Producto de un vector fila con un vector columna"
    print("Un vector fila:")
    vector1 = list(map(float, input().split()))
    print("Un vector columna:")
    vector2 = list(map(float, input().split()))

    Point = sum([xt*yt for xt, yt in zip(vector1, vector2)])
    print("Resultado:", Point)


def Multipl_VColumn_VFile():
    "Producto de un vector columna con un vector fila"
    print("Un vector columna:")
    vector1 = list(map(float, input().split()))
    print("Un vector fila:")
    vector2 = list(map(float, input().split()))

    matriz = []
    for var in vector1:
        fila = []
        for valy in vector2:
            fila.append(var*valy)
        matriz.append(fila)
    print("Resultado:")
    print(numpy.array(matriz))


def invertirMatriz():
    "De matriz a matriz invertida"
    # Esta funcion aplica en matriz 2x2
    print("Imprime la matriz")
    matriz = []
    for _ in range(2):
        matriz.append(list(map(float, input().split())))

    matriz_f = invertMatriz_re(matriz)
    print("Matriz invertida:")
    print(numpy.array(matriz_f))


def determinantes():
    "Determinante de una matriz"
    n = int(input("Rango: "))
    print("Imprime la matriz")
    matriz = []
    for _ in range(n):
        matriz.append(list(map(float, input().split())))

    determ = determinanteMajor(matriz, n)
    print("Determinante:", determ)

def condicionmaineto():
    "Condicionamiento de una matriz"
    rangocolum = int(input("Rango de la columna: "))
    matriz = []
    print("Imprime un vetor o matriz: ")
    for _ in range(rangocolum):
        matriz.append(list(map(float, input().split())))

    if rangocolum == 1 or len(matriz[0]) == 1:
        Point = sum([xt**2 for xt in matriz])
        normafinal = math.sqrt(Point)
        print("Su norma es:", normafinal) 
        print("No se puede hallar el condicionamiento")
    else:
        Point = []
        for fiel in Transposicion(matriz):
            pass
        pass
    Point_inv = sum([xt*yt for xt, yt in zip(invertMatriz_re(matriz), invertMatriz_re(matriz))])


# FACTORIXACION DE MATRICES
# -----------------------------
def met_Gram_Schmidt():
    # Solo con matrices m x 2
    n = int(input("Rango: "))
    print("Imprime la matriz")
    matriz = []
    for _ in range(n):
        matriz.append(list(map(float, input().split())))
    # norma de la fila 1
    v1 = fila1 = [x[0] for x in matriz]   # v1 = a1 : [2 0 0]
    r11 = math.sqrt(sum([xt**2 for xt in fila1])) # r11 : 2
    q1 = [fil/r11 for fil in v1]  # columna  q1 : [1 0 0]

    fila2 = [x[1] for x in matriz] # a2 : [0 0 -1]
    r12 = sum([xt*yt for xt, yt in zip(q1, fila2)]) # r12 : 0

    v2 = [der-pr for der, pr in zip(fila2, [r12*fr for fr in q1])]  # columna
    r22 = math.sqrt(sum([xt**2 for xt in v2]))
    q2 = [ref/r22 for ref in v2]  # columna
    Qvalue = Transposicion([q1, q2])
    Rvalue = [[r11, r12], [0, r22]]
    print("Factores matrices:")
    print("Q--\n", numpy.array(Qvalue))
    print("R--\n", numpy.array(Rvalue))


def met_Doolittle():
    # La matriz tiene que ser de orden paralela
    n = int(input("Rango: "))
    print("Imprime la matriz")
    matriz = []
    for _ in range(n):
        matriz.append(list(map(float, input().split())))
    triang, multiplos = EliminGaussiPiv(matriz)  # matriz U

    ident = identidad(n)    # matriz L
    for val, mult in zip(ident, multiplos):
        for num, mt in zip(val, mult):
            if num == 0:
                val[val.index(num)] = mt
    print("Mtarices factores:")
    print("L--", numpy.array(Transposicion(ident)))
    print("U--", numpy.array(triang))

def met_Crout():
    pass



# productoPunto()
# productoMatriz()
# determinantes()
# Multipl_VColumn_VFile()
# invertirMatriz()
met_Gram_Schmidt()