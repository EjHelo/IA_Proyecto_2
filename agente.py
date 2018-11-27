
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

    def set_estrategias(self, lista_estrategias):
        self.secuencia = lista_estrategias[0]
        self.centro = lista_estrategias[1]
        self.fila = lista_estrategias[2]
        self.par = lista_estratefias[3]

    def get_estrategias(self):
        return [self.secuencia,self.centro,self.fila,self.par]

    def estrategias_to_string(self):
        string = '['+str(self.secuencia)+','+str(self.centro)+','+str(self.fila)+','+str(self.par)+']'
        print( string)
    
    def set_victorias(self, numero):
        self.victorias = numero
    def incrementar_victorias(self):
        self.victorias += 1
    def get_victorias(self):
        return self.victorias
    def set_pieza(self,pieza):
        self.pieza = pieza
    def get_pieza(self):
        return self.pieza

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
        '''print("Centro vs Extremo",lista)
        print("Secuencia espacio",secuencia)
        print("fila, columna",fila)
        print("par, impar",par)'''
        #print("as ",self.eliminar_repetidos(lista,secuencia,fila,par))
        check = self.eliminar_repetidos(lista,secuencia,fila,par)
        respuesta = self.validar_columnas(tablero,check)
        #print(respuesta)
        return respuesta

    def validar_columnas(self,tablero,lista):
        aux = []
        for i in lista:
            if  tablero.columna_valida(i):
                aux+=[i]
        
        return aux
        
    def eliminar_repetidos(self,centro_extremo, secuencia_espacio, fila_columna, par_impar):
        columnas=[]
        columnas = list(set(centro_extremo+secuencia_espacio+fila_columna+par_impar))
        return columnas
                

    def funcion_costo(self, tablero, columnas_estrategia):
        minimax = Minimax(tablero, columnas_estrategia)
        return minimax.mejor_movimiento(tablero, self.pieza)


    








    
