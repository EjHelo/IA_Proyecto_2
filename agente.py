
# generate random integer values
from random import seed
from random import random

class Agente:

    def __init__(self, secuencia_espacio, centro_extremo, fila_columna, bloquear, pieza ):
        self.secuencia = secuencia_espacio
        #self.espacio= 1-secuencia_espacio
        self.centro= centro_extremo
        #self.extremo= 1-centro_extremo
        self.fila = fila_columna
        #self.columna= 1-fila_columna
        self.bloquear = bloquear
        self.victorias = 0
        self.pieza = pieza

    def escoger_columnas(self, tablero, pieza):
        #buscar caracteristicas en tablero
        lista = []
        secuencia = []
        fila = []
        columna = []
        seed(2)

        ctr = random()
        if ctr <= self.centro:
            lista= [3,4,5]
        else:
            lista= [1,2,6,7]
        
        sec = random()
        if(sec <= self.secuencia):
            secuencia = tablero.get_lista_secuencia(self.pieza)
        else:
            secuencia = tablero.get_lista_espacio(self.pieza)
            
        row = random()
        if row <= self.fila:
            fila = tablero.get_lista_fila(self.pieza)
        else:
            columna = tablero.get_lista_columna(self.pieza)
        print(lista)
        print(secuencia)
        print(columna)
        print(fila)
        print(ctr)
        print(sec)
        print(row)
        return lista
        
        
        

    def realizar_movida(self,tablero):
        #funcion de costo para las columnas
        #tiene q devolver tablero
        pass

    def funcion_costo(self):
        pass
