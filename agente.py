
# generate random integer values
from random import seed
from random import random

class Agente:

    def __init__(self, secuencia_espacio, centro_extremo, fila_columna, bloquear ):
        self.secuencia = secuencia_espacio
        #self.espacio= 1-secuencia_espacio
        self.centro= centro_extremo
        #self.extremo= 1-centro_extremo
        self.fila = fila_columna
        #self.columna= 1-fila_columna
        self.bloquear = bloquear
        self.victorias = 0

    def escoger_columnas(self):
        #buscar caracteristicas en tablero
        pass

    def realizar_movida(self,tablero):
        #funcion de costo para las columnas
        #tiene q devolver tablero
        pass

    def funcion_costo(self):
        pass
