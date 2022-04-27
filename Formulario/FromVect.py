import math

def productoCruz_re(vector1, vector2):
    # producto cruz entre dos vectores
    resultante = []
    for i in range(3):
        muest1, muest2 = vector1.copy(), vector2.copy()
        muest1.pop(i)
        muest2.pop(i)
        res = (muest1[0]*muest2[1])-(muest2[0]*muest1[1])
        resultante.append(round(res,2))
    return resultante # en vector

def modulo_re(vector):
    # modulo de un vector
    return math.sqrt(sum([x**2 for x in vector])) # en escalar

def productoPunto_re(vector1:list[float], vector2:list[float]):
    # producto punto de dos vectores
    return sum([xt*yt for xt, yt in zip(vector1, vector2)]) # en escalar

def vector_unit(rang:list[str], vector, modulo:float):
    # halla los angulos directivos de cada componente x y z
    for val, vect in zip(rang, vector):
        # vector unitario
        vector = vect/modulo
        # angulo directivos
        angle = math.acos(vector)*(180/math.pi)
        print(f"--- Vector {round(vector, 2)}{val} con angulo {round(angle, 2)}")

def anguloPer_vector(point:float, modulo1, modulo2):
    angle = math.acos(point/(modulo1*modulo2))
    ang_sex = angle*(180/math.pi)
    return ang_sex # en angulo sexagesimal

def ProyecCompon_re(vector1:list[float], vector2:list[float]):
    # componente de vector1 sobre vector2
    componente = productoPunto_re(vector1, vector2)/modulo_re(vector2)
    print("Componente:", round(componente,2))
    # proyeccion del vector componente
    vector_unit = [vect/modulo_re(vector2) for vect in vector2]
    proyeccion = [round(componente*el,2) for el in vector_unit]
    print("Proyeccion:", proyeccion)

def ThreePointEC(pt1:list, pt2:list, pt3:list):
    # vector pt1-pt2
    v_pt1_pt2 = [b-a for b, a in zip(pt2, pt1)]
    # vector pt2-pt3
    v_pt2_pt3 = [c-b for b, c in zip(pt3, pt2)]
    v_n = productoCruz_re(v_pt1_pt2, v_pt2_pt3)
    return EcuacionPlano_re(v_n, v_pt2_pt3)

def EcuacionPlano_re(perpen, vecc):
    indep = []
    for num, var in zip(perpen, ["x", "y", "z"]):
        tre = "+" if num >= 0 else "-"
        ig = f"{tre} {abs(round(num, 2))}{var}"
        indep.append(ig)
    const = [vec*num for vec, num in zip(vecc, perpen)]
    plano = ""
    for i, cs in zip(indep, const):
        valid = "+" if cs >= 0 else "-"
        plano += f"{i} {valid} {abs(round(cs, 2))} "
    return plano