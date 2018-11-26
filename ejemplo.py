from tablero import Tablero
from agente import Agente

def jugar():
    tablero = Tablero(6,7)
    agente1 = Agente (1,1,1,1,1)

    columna = int(input("Jugador 1 selecione una columna (1 - 7): ")) -1
    tablero.colocar_pieza(0,1,1)
    seleccion = agente1.escoger_columnas(tablero, 1)
    
