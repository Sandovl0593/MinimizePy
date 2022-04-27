# Usado para relaciones en A (AxA)


def reflexive(conjunt):
    num_tup = []
    pares_equal = 0
    for tuple in conjunt:
        if tuple[0] == tuple[1]:
            if tuple not in num_tup:
                num_tup.append(tuple)
            pares_equal += 1
    if pares_equal == len(num_tup):
        return True
    return False


def transitive(conjunt):
    if len(conjunt) <= 1:
        return True
    trans = 0
    for i in range(len(conjunt)):
        x1, y1 = conjunt[i]
        for iter in conjunt:
            x2, y2 = iter
            if y1 == x2:
                if (x1, y2) in conjunt:
                    trans += 1
    if trans >= 1:
        return True
    return False


def simetric(conjunt):
    num_tup = []
    for tuple in conjunt:
        x, y = tuple
        if tuple not in num_tup:
            num_tup.append((x, y))
            num_tup.append((y, x))

    pares_sim = 0
    for tuple in conjunt:
        x, y = tuple
        if (y, x) in conjunt:
            pares_sim += 1

    if pares_sim == len(num_tup) or len(conjunt) >= len(num_tup):
        return True
    return False


def antisimetric(conjunt):
    valued = False
    for tuple in conjunt:
        x, y = tuple 
        if (y, x) in conjunt:
            if x == y:
                valued = True
            else:
                valued = False
        else:
            if x != y:
                valued = True
    return valued

prueba = [(3,2), (3, 3), (2,1), (1,1), (2,2)]

print("Conjunto:", str(prueba))
print("Es reflexiva" if reflexive(prueba) else "No es reflexiva")
print("Es simétrica" if simetric(prueba) else "No es simétrica")
print("Es transitiva" if transitive(prueba) else "No es transitiva")
print("Es antisimétrica" if antisimetric(prueba) else "No es antisimétrica")
print("Es equivalente" if reflexive(prueba) and simetric(prueba) and transitive(prueba) else "No es equivalente")
print("Es una orden parcial" if reflexive(prueba) and antisimetric(prueba) and transitive(prueba) else "No es una orden parcial")