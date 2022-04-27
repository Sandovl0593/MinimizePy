import numpy

def Columnacion(matriz):
    "Distribuir columnas en listas horizontales"
    filas_matriz2 = []
    for i in range(len(matriz[0])):
        indice_matriz = []
        for colum in matriz:
            indice_matriz.append(colum[i])
        filas_matriz2.append(indice_matriz)
    return filas_matriz2

def Transposicion(matriz):
    "Indexar la lista de columnas en columnas verticales"
    posicion = []
    columnas = len(matriz[0])
    for i in range(columnas):
        posicion.append([])
    for j in range(len(matriz)):
        for i in range(columnas):
            posicion[i].append(matriz[j][i])
    return posicion

def productoMatriz_re(matriz1, matriz2):
    filas_matriz = Columnacion(matriz2)
    sum_filmatriz1 = []
    for distrib in filas_matriz:
        colum_result = []
        for divid in matriz1:
            num_parc = []
            for num1, num2 in zip(divid, distrib):
                num_parc.append(num1*num2)
            colum_result.append(round(sum(num_parc), 2))
        sum_filmatriz1.append(colum_result)
    matriz_final = Transposicion(sum_filmatriz1)
    return matriz_final

def invertMatriz_re(matriz):
    matrizmej = matriz
    aux1 = matrizmej[1][1]
    matrizmej[1][1] = matrizmej[0][0]
    matrizmej[0][0] = aux1

    aux2 = matrizmej[1][0]
    matrizmej[1][0] = int(- matrizmej[0][1])
    matrizmej[0][1] = int(- aux2)
    return matrizmej

def determinanteMajor(matriz:list, long:int):
    "Determinante de una matriz de n x n"
    # Aplica a matrices de longitud paralela
    if long == 2:
        return (matriz[0][0]*matriz[1][1])-(matriz[1][0]*matriz[0][1])
        
    operator = []
    dex = int(input((f"Orden de subfila {long}x{long}:")))
    long_n = long-1
    for i in range(long):
        muest = matriz.copy()
        muest.pop(dex)
        for file in muest:
            file.pop(i)

        resolution = matriz[0][i] * ((-1)**(long_n+i+1)) * determinanteMajor(muest, long_n)
        operator.append(resolution)

    return sum(operator)

def EliminGaussiNoPiv(matriz:list[list]):
    "Matriz triangular superior sin pivoteo"
    n = len(matriz[0])-1
    for k in range(n-1):
        pivote = matriz[k][k]
        for j in range(k+1,n):
            mjk = matriz[j][k]/pivote
            resol = [round(jen-(mjk*ken), 4) for jen, ken in zip(matriz[j], matriz[k])]
            matriz[j] = resol
    return matriz

def EliminGaussiPiv(matriz:list[list]):
    "Matriz triangular superior con pivoteo"
    m = len(matriz)
    n = len(matriz[0])-1
    multip = []
    for k in range(n-1):
        column = [f[k] for f in matriz]
        pos = column.index(max([abs(matriz[i][k]) for i in range(k, m)]))
        aux = matriz[pos]
        matriz[pos] = matriz[k]
        matriz[k] = aux
        pivote = matriz[k][k]
        listmult = []
        for j in range(k+1, m):
            mjk = matriz[j][k]/pivote
            resol = [round(jen-(mjk*ken), 4) for jen, ken in zip(matriz[j], matriz[k])]
            matriz[j] = resol
            listmult.append(mjk)
        multip.append(listmult)
    return matriz, multip

def ResolSistem(matriz:list[list]):
    "Resolucion de sistema de ecuaciones con matrices"
    print("1-- Con pivoteo--\n2-- Sin pivoteo\n")
    ded = input("-- ")
    if ded == '1':
        result, multp = EliminGaussiPiv(matriz)
    elif ded == '2':
        result = EliminGaussiNoPiv(matriz)

    print("Hecho..\nDevolver vector columna? 1 o 0")
    des = input("-- ")
    if des == '1':
        Number = [lis[-1] for lis in result]  # vector columna
        for lis in result:
            lis.pop(-1)
        return result, Number
    elif des == '0':
        return result

def sustitucRg(matEsc, colum):
    "Solucion del sistema escalonado"
    n = len(matEsc[0])
    x = [0 for _ in range(n)]  # vector columna
    for k in range(n-1, 0, -1):
        UU = matEsc[k][k+1:n]
        xU = x[k+1:n]
        fred = (colum[k]- sum([x*y for x,y in zip(UU, xU)]))/matEsc[k][k]
        print(fred)

def identidad(long):
    matriz = []
    for i in range(long):
        submat = [1 if i == j else 0 for j in range(long)]
        matriz.append(submat)
    return matriz
