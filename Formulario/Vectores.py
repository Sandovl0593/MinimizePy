import math
from FromVect import *

# RESOLUCION DE VECTORES
# ---------------------
def productoCruz():
    # OJO: solo ocuure con vetores de tres dimensiones
    print("Imprime dos vectores")
    vector1 = list(map(float, input().split()))
    vector2 = list(map(float, input().split()))

    resultante = productoCruz_re(vector1, vector2)
    print("Producto cruz:", resultante)


def productoPunto():
    print("Imprime dos vectores:")
    vector1 = list(map(float, input().split()))
    vector2 = list(map(float, input().split()))

    # Modulos de los dos vectores:
    modulo1, modulo2 = modulo_re(vector1), modulo_re(vector2)
    print("Modulo Vec1:", modulo1)
    print("Modulo Vec2:", modulo2)
    
    # Producto punto
    point = productoPunto_re(vector1, vector2)
    print("Producto punto:", round(point, 2))

    # angulo entre dos vectores
    ang_sex = anguloPer_vector(point, modulo1, modulo2)
    print("Ángulo formado:", round(ang_sex, 2))

    if len(vector1) == 2 and len(vector2) == 2:
        rang = ["i", "j"]
    else:
        rang = ["i", "j", "k"]

    #vectores unitarios con sus angulos directivos
    print("Vector 1:")
    vector_unit(rang, vector1, modulo1)
    
    print("Vector 2:")
    vector_unit(rang, vector2, modulo2)


def triplePuntoPunto():
    print("Imprime tres vectores")
    # Los vectores deben ser tridimensionales
    vector1 = list(map(float, input().split()))
    vector2 = list(map(float, input().split()))
    vector3 = list(map(float, input().split()))

    poinrre = productoCruz_re(vector2, vector3)
    # modulee = modulo_re(vector1)
    result = productoPunto_re(vector1, poinrre)
    print("Triple producto escalar:")
    print(round(result, 2))


def proy_conpon():
    print("Imprime dos vectores")
    vectorA = list(map(float, input().split()))
    vectorB = list(map(float, input().split()))

    print("De A sobre B:  1\nDe B sobre A.  2\nEscoge opcion")
    opcion = int(input("Opcion: "))
    print()
    if opcion == 1:
        ProyecCompon_re(vectorA, vectorB)
    elif opcion == 2:
        ProyecCompon_re(vectorB, vectorA)


def VectOneParam():
    # vector pendiente
    print("Vector -r0:")
    vector_r = list(map(float, input().split()))
    # vector posicion
    print("Vector -v:")
    vector_v = list(map(float, input().split()))
    print("Ecuaciones parametricas:")
    for r, v, ig in zip(vector_r, vector_v, ["x", "y", "z"]):
        isn = "+" if r >= 0 else "-"
        sig = "+" if v >= 0 else "-"
        print(f"{ig} = {isn} {abs(round(r, 2))} {sig} {abs(round(v, 2))} t")


def EcuacionPlano():
    print("Escoge tipo de problema:\n1: tres puntos\n2: punto - perpendicular")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        pt1 = list(map(float, input("Punto A: ").split()))
        pt2 = list(map(float, input("Punto B: ").split()))
        pt3 = list(map(float, input("Punto C: ").split()))
        plano = ThreePointEC(pt1, pt2, pt3)
    elif opcion == 2:
        #vector perpendicular 
        perpen = list(map(float, input("vector perp: ").split()))
        vecc = list(map(float, input("Punto: ").split()))
        plano = EcuacionPlano_re(perpen, vecc)
    print("Ecuacion del plano:", plano)


def distancePuntoRecta():
    # distacia de un punto y una recta
    punto = list(map(float, input("Un punto: ").split()))
    print("Imprime ecuaciones parametricas")
    ec1 = list(map(float, input("1- Constante y mult: ").split()))
    ec2 = list(map(float, input("2- Constante y mult: ").split()))
    ec3 = list(map(float, input("3- Constante y mult: ").split()))
    vect_pos = [ec1[1], ec2[1], ec3[1]]
    vectorPS = [ec1[0], ec2[0], ec3[0]]
    vectorPS = [ded-pos for ded, pos in zip(punto, vectorPS)]
    prod = productoCruz_re(vect_pos, vectorPS)
    dist = modulo_re(prod)/modulo_re(vect_pos)
    print("Distancia de:", round(dist, 2))


# productoCruz()
# VectOneParam()
# productoPunto()
# EcuacionPlano()
# proy_conpon()
# triplePuntoPunto()
distancePuntoRecta()