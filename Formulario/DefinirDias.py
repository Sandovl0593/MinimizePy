def bisiesto(año:int):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

def validarDias(dia, mes, listMes:list):
    if (listMes[mes-1] < dia or dia <= 0) or (mes <= 0 or mes > 12):
        return True
    return False

def contarDias(dia1, dia2, mes1, mes2, meses:list):
    diasAcu:int = 0
    if mes1 != mes2:
        diasAcu += (meses[mes1-1] - dia1)
        for di in range(mes1, mes2-1):
            diasAcu += meses[di]
        diasAcu += dia2
    else:
        diasAcu += (dia2 - dia1)
    return diasAcu

def obtenerDias(fechaInicio:str, fechaFinal:str):
    dia1, mes1, año1 = (int(x) for x in fechaInicio.split("/")) 
    dia2, mes2, año2 = (int(x) for x in fechaFinal.split("/")) 

    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mesAn1, mesAn2 = meses, meses
    if bisiesto(año1):
        mesAn1[1] = 29
    if bisiesto(año2):
        mesAn2[1] = 29
    
    if año2 < año1:
        raise OverflowError
    if validarDias(dia1, mes1, mesAn1) or validarDias(dia2, mes2, mesAn2):
        raise OverflowError

    diasAcu = 0
    if año2 == año1:
        diasAcu += contarDias(dia1, dia2, mes1, mes2, mesAn2)
    else:
        diasAcu += contarDias(dia1, 31, mes1, 12, mesAn1)
        for di in range(1, año2-año1-1):
            diasAcu += 365
            if bisiesto(año1 + di):
                diasAcu += 1
        diasAcu += contarDias(0, dia2, 1, mes2, mesAn2) 
        
    return diasAcu

while True:
    try:
        fecha1 = input("Ingrese fecha inicial: ")
        fecha2 = input("Ingrese fecha final: ")
        horas = int(input("Horas por día: "))
        dias_falt = obtenerDias(fecha1, fecha2)
        break
    except ValueError as err:
        print("Coloque las datos correctamente...!")
        print("-----------------------------------")
    except OverflowError as err:
        print("Fecha inválida...!")
        print("-------------------")
    except IndexError as err:
        print("Fecha inválida...!")
        print("-------------------")

print("--------------------")
print(f"Dias faltantes: {dias_falt}\nHoras acumuladas: {dias_falt*horas}")