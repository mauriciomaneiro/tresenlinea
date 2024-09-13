def imprimir_tablero(tablero):
    for fila in tablero:        
        print(" | ".join(fila))
        print("-" * 10)

def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if all([celda == jugador for celda in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def juego_tres_en_raya(puntajes):
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    movimientos = 0

    while movimientos < 9:
        imprimir_tablero(tablero)
        jugador_actual = jugadores[turno]
        print(f"Turno del jugador {jugador_actual}")

        fila = int(input("Ingresa la fila (0, 1, 2): "))
        columna = int(input("Ingresa la columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            movimientos += 1

            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                puntajes[jugador_actual] += 1
                return

            turno = 1 - turno
        else:
            print("Movimiento inválido, intenta de nuevo.")

    imprimir_tablero(tablero)
    print("¡Es un empate!")

if __name__ == "__main__":
    puntajes = {"X": 0, "O": 0}
    while True:
        juego_tres_en_raya(puntajes)
        print(f"Puntajes: {puntajes}")
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ")
        if jugar_de_nuevo.lower() != "s":
            break
