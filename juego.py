from tablero import Tablero
from agente import Agente

class Juego:

    def __init__(self):
        self.tablero = Tablero(6,7)
        self.agente1 = Agente(1,1,1,1,1)
        self.agente2 = Agente(1,1,1,1,2)

    def jugar(self):
        self.tablero.colocar_pieza(0,1,1)
        lista = self.agente1.escoger_columnas(self.tablero, 1)
        self.tablero.print_tablero()

    
