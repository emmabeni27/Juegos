import random

inicio = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
for linea in inicio:
    print(linea)
fichas = ["O", "X"]
ficha_compu = random.choice(fichas)
if ficha_compu == "X":
    ficha_jugador = "O"
else:
    ficha_jugador = "X"
print(f"Ficha de la computadora: {ficha_compu}\nFicha del jugador: {ficha_jugador}")
# lista de posiciones libres e ir restando
posiciones_libres = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]


def jugar(posiciones_libres, inicio, ficha_jugador, ficha_compu):

    fila_jugador = input("Ingrese número de fila: ")
    fj=int(fila_jugador)-1
    columna_jugador = input("Ingrese número de columna: ")
    cj=int(columna_jugador)-1
    inicio[fj][cj] = ficha_jugador
    posicion_jugador = fila_jugador + columna_jugador
    if posicion_jugador in posiciones_libres:
        posiciones_libres.remove(posicion_jugador)

    fila_compu = random.choice(["1", "2", "3"])
    fc=int(fila_compu)-1
    columna_compu= random.choice(["1", "2", "3"])
    cc=int(columna_compu)-1
    while inicio[fc][cc]!="_":
        fila_compu = random.choice(["1", "2", "3"])
        fc = int(fila_compu) - 1
        columna_compu = random.choice(["1", "2", "3"])
        cc = int(columna_compu) - 1
    inicio[fc][cc] = ficha_compu

    posicion_compu = fila_compu + columna_compu
    if posicion_compu in posiciones_libres:
        posiciones_libres.remove(posicion_compu)

    for linea in inicio:
        print(linea)

    if inicio[0][0]==inicio[0][1]==inicio[0][2]==ficha_jugador or inicio[1][0]==inicio[1][1]==inicio[1][2]==ficha_jugador or inicio[2][0]==inicio[2][1]==inicio[2][2]==ficha_jugador or inicio[0][0]==inicio[1][0]==inicio[2][0]==ficha_jugador or inicio[0][1]==inicio[1][1]==inicio[2][1]==ficha_jugador or inicio[0][2]==inicio[1][2]==inicio[2][2]==ficha_jugador or inicio[0][0]==inicio[1][0]==inicio[2][0]==ficha_jugador or inicio[0][0]==inicio[1][1]==inicio[2][2]==ficha_jugador or inicio[2][0]==inicio[1][1]==inicio[0][2]==ficha_jugador:
        print("Usted ganó :)")
    elif inicio[0][0]==inicio[0][1]==inicio[0][2]==ficha_compu or inicio[1][0]==inicio[1][1]==inicio[1][2]==ficha_compu or inicio[2][0]==inicio[2][1]==inicio[2][2]==ficha_compu or inicio[0][0]==inicio[1][0]==inicio[2][0]==ficha_compu or inicio[0][1]==inicio[1][1]==inicio[2][1]==ficha_compu or inicio[0][2]==inicio[1][2]==inicio[2][2]==ficha_compu or inicio[0][0]==inicio[1][0]==inicio[2][0]==ficha_compu or inicio[0][0]==inicio[1][1]==inicio[2][2]==ficha_compu or inicio[2][0]==inicio[1][1]==inicio[0][2]==ficha_compu:
        print("Usted perdió :(")
    else:
        jugar(posiciones_libres, inicio, ficha_jugador, ficha_compu)


jugar(posiciones_libres, inicio, ficha_jugador, ficha_compu)