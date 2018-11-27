from tablero import Tablero
from agente import Agente

def jugar():
    tablero = Tablero(6,7)
    agente1 = Agente (1,1,1,1,1)

    columna = int(input("Jugador 1 selecione una columna (1 - 7): ")) -1
    tablero.colocar_pieza(0,1,1)
    seleccion = agente1.escoger_columnas(tablero, 1)
    
agente = Agente(1,1,1,1,2)
tablero = Tablero(6,7)
tablero.crear_tablero()
tablero.colocar_pieza(0,0,1)
tablero.colocar_pieza(0,1,1)
tablero.colocar_pieza(0,2,2)
tablero.colocar_pieza(0,3,1)
tablero.colocar_pieza(0,4,2)
tablero.colocar_pieza(0,5,1)
tablero.colocar_pieza(1,1,1)
tablero.colocar_pieza(1,2,2)
tablero.colocar_pieza(1,3,2)
tablero.colocar_pieza(1,4,2)
    #Ejecución
resultado = agente.escoger_columnas(tablero)
    #Aserión
print(resultado)
