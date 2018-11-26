
# generate random integer values
from random import seed
from random import random

from minimax import Minimax

import copy

class Agente:

    def __init__(self, secuencia_espacio, centro_extremo, fila_columna, par_impar, pieza ):
        self.secuencia = secuencia_espacio
        #self.espacio= 1-secuencia_espacio
        self.centro= centro_extremo
        #self.extremo= 1-centro_extremo
        self.fila = fila_columna
        #self.columna= 1-fila_columna
        self.par = par_impar
        self.victorias = 0
        self.pieza = pieza

    def ganar(self, tablero):
        columna = tablero.get_columna()
        
        for col in range(columna):
            temp_tablero = copy.deepcopy(tablero)
            if temp_tablero.columna_valida(col):
                # Simula jugada
                fila = temp_tablero.get_fila_abierta(col)
                temp_tablero.colocar_pieza(fila, col, self.pieza)
                if temp_tablero.movimiento_gane(self.pieza):
                    # Si tiene gane realiza la jugada de gane y retorna el tablero
                    tablero.colocar_pieza(fila, col, self.pieza)
                    return tablero, True
        return tablero,False


    def bloquear(self, tablero):
        oponente = 0
        if self.pieza == 1:
            oponente = 2
        else:
            oponente = 1

        columna = tablero.get_columna()
        for col in range(columna):
            temp_tablero = copy.deepcopy(tablero)
            if temp_tablero.columna_valida(col):
                # Simula jugada
                fila = temp_tablero.get_fila_abierta(col)
                temp_tablero.colocar_pieza(fila, col, oponente)
                if temp_tablero.movimiento_gane(oponente):
                    # Si tiene gane realiza la jugada de bloqueo y retorna el tablero
                    tablero.colocar_pieza(fila, col, self.pieza)
                    return tablero, True
        return tablero, False
        

    def escoger_columnas(self, tablero):
        #buscar caracteristicas en tablero
        lista = []
        secuencia = []
        fila = []
        columna = []
        par = []
        seed(2)

        ctr = random()
        if ctr <= self.centro:
            lista= [2,3,4]
        else:
            lista= [0,1,5,6]
        
        sec = random()
        if(sec <= self.secuencia):
            secuencia = tablero.get_lista_secuencia(self.pieza)
        else:
            secuencia = tablero.get_lista_espacio(self.pieza)
            
        row = random()
        if row <= self.fila:
            fila = tablero.get_lista_fila(self.pieza)
        else:
            fila = tablero.get_lista_columna(self.pieza)

        even = random ()
        if even <= self.par:
            par = [1,3,5]
        else:
            par = [0,2,4,6]
        print(lista)
        print(secuencia)
        print(fila)
        print(par)
        print(self.eliminar_repetidos(lista,secuencia,fila,par))
        return self.eliminar_repetidos(lista,secuencia,fila,par)

        
    def eliminar_repetidos(self,centro_extremo, secuencia_espacio, fila_columna, par_impar):
        columnas=[]
        default = list(set(centro_extremo).intersection(par_impar))
        if(secuencia_espacio!=[]):
            if(fila_columna!=[]):
                aux = list(set(default).intersection(secuencia_espacio))
                columnas = list(set(aux).intersection(fila_columna))
            else:
                columnas = list(set(default).intersection(secuencia_espacio))
        else:
            if(fila_columna!=[]):
                columnas = list(set(default).intersection(fila_columna))
            else:
                columnas = default
        if columnas==[]:
            return default
        return columnas
                

    def funcion_costo(self, tablero, columnas_estrategia):
        minimax = Minimax(tablero, columnas_estrategia)
        return minimax.mejor_movimiento(tablero, self.pieza)


    








    
