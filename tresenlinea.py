#Función para imprimir el trablero que se recibe. 
def imprimir_tablero(tablero):
    
    print("  1   2   3")
    #Se recorre cada fila en tablero.
    for i in range(len(tablero)):
        #Esta línea une cada elemento de la fila con un " | " en medio.
        print(f"{filas[i]} {' | '.join(tablero[i])}")
        #Esta linea imprime 10 " - " para separar visualmente cada fila que vamos imprimiendo.
        if i < len(tablero) - 1:
            print(f"  {'-' * 10}")
    print("\n")


#Esta función toma el tablero y el jugador, recorre el tablero y verifica si hay un ganador.
def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales. Recorre 3 veces.
    for i in range(3):
        #Devuelve verdadero si: todas las celdas de una fila equivalen a "X" o "O". 
        #En la segunda condicion del or, revisa que todas las celdas de una columna sean iguales a "X" o "O"
        # for celda in tablero[i]:
        #     if celda != jugador:
        #         return False
            
        #     pass
        if all([celda == jugador for celda in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):
            return True
    #Revisa que los jugadores hayan hecho "ta-te-ti" en diagonal.
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    #Si ninguna de estas condiciones se cumple, la función llega a este punto y devuelve False, el juego sigue.
    return False


def validar_coordenadas(coordenadas: str, filas: list[str], columnas: list[str]) -> bool:
    # Se valida que las coordenadas coincidan con las filas y columnas posibles
    return coordenadas[0].lower() in filas and coordenadas[1] in columnas


#Esta función inicia las variables turno, movimientos, jugadores y ademas genera el tablero.
def juego_tres_en_raya(puntajes):
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0
    movimientos = 0

    #Mientras movimientos sea menor a 9, los jugadores podrán seguir jugando. 
    # Al momento de que movimientos sea 9, el tablero se verá completo.
    while movimientos < 9:
        #Llamamos a la función tablero
        imprimir_tablero(tablero)
        #El jugador actual va a corresponder a "X" o "O" dependiendo si turno es 0 o 1.
        jugador_actual = jugadores[turno]
        #Hacemos uso del f-string para imprimir el valor de la variable jugador_actual.
        print(f"Turno del jugador {jugador_actual}")

        #Le pedimos el valor de la fila y columna en la que quiere jugar el jugador_actual.
        while True:
            coordenadas = input("Ingrese la Fila (Letras: a, b, c) y Columna (Numeros: 1, 2, 3). Ejemplo 'a3': ")

            if len(coordenadas) == 2:
                if not(validar_coordenadas(coordenadas, filas, columnas)):
                    print(f"La Coordenada '{coordenadas}' es incorrecta, intenta de nuevo.")
                    continue
                else:
                    break
            else:
                print(f"La Coordenada '{coordenadas}' es incorrecta, intenta de nuevo.")
                
        fila = filas.index(coordenadas[0])
        columna = columnas.index(coordenadas[1])

        #Verificamos que la ubicación este vacia y si es asi, le asignamos el valor de "X" o "O"
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            #Sumamos 1 al contador de movimientos.
            movimientos += 1

            #Si verificar_ganador es verdadero, se ingresa al if.
            if verificar_ganador(tablero, jugador_actual):
                #Se vuelve a imprimir el tablero en el que se deberia ver 3 en linea.
                imprimir_tablero(tablero)
                #Se utiliza el f-string para imprimir el valor de jugador_actual
                # en el mensaje de ganador.
                print(f"¡El jugador {jugador_actual} ha ganado!")
                #Se suma 1 al jugador, con la finalidad de darle un sistema de puntos al juego.
                puntajes[jugador_actual] += 1
                return

            turno = 1 - turno
        #Si la ubicación no equivale a " ", es decir que no está vacia, se entra al else.
        else:
            print("Movimiento inválido, intenta de nuevo.")

    #Si movimientos es 9, se llega a este punto dado a que no se puede ocupar ningún lugar mas
    # y se da un empate.
    imprimir_tablero(tablero)
    print("¡Es un empate!")


def imprimir_puntajes(puntajes: dict) -> None:
    print(f"""Tabla de Puntajes:
{'-'*20}
Jugador X: {puntajes["X"]} Puntos
Jugador O: {puntajes["O"]} Puntos""")


def creditos():
    conjunto = {
        "Ariel Tapia", 
        "Mauricio Maneiro", 
        "Fabricio Capone", 
        "Agustin Blasco",
    }

    print("\nJuego desarrollado por el Grupo 1. Miembros:")
    for nombre in conjunto:
        print(f"- {nombre}")


def main():
    while True:
        juego_tres_en_raya(puntajes)
        #Imprimimos el diccionario puntajes.
        imprimir_puntajes(puntajes)
        #Se pregunta si se desea jugar de nuevo, hacemos uso de .lower() en caso de que el usuario
        #ingrese un caracter en mayúscula.
        jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ")
        #Si el valor no es igual a "s", se entra al if y con el break salimos del while.
        if jugar_de_nuevo.lower() != "s":
            creditos()
            break


#Esta linea asegura que este bloque de codigo se corra solamente si se ejecuta este archivo.
#En cambio, si esto es importado como modulo este bloque no correria automaticamente.
if __name__ == "__main__":
    #Usamos un Diccionario para tener el valor las partidas ganadas por jugador.
    puntajes = {"X": 0, "O": 0}

    # Se definen las Filas y Columnas posibles
    filas = ["a", "b", "c"]
    columnas = ["1", "2", "3"]

    main()
