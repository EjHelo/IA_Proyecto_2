from tablero import Tablero
from agente import Agente

from random import seed
from random import random

import numpy
from optparse import OptionParser


parser = OptionParser()

parser.add_option("", "--humano-maquina", action="store_true", dest="humano_maquina", default=False, help="Seleciona modalidad de juego humano vs maquina")
parser.add_option("", "--maquina-maquina", action="store_true", dest="maquina_maquina", default=False, help="Seleciona modalidad de juego maquina vs maquina")

(opciones, args) = parser.parse_args()

if opciones.humano_maquina:

    tablero = tablero(6,7)
    agente = Agente(1,1,1,1,2)
    turn = 1
    tablero.print_tablero()
    print(" Inicia Humano, jugador 1 ")
    while not tablero.tablero_lleno():
        
        # Turno del humano
        if turn == 1:
            columna = int(input("Jugador 1 selecione una columna (1 - 7): ")) -1
            if columna > 6 or columna < 0 or (not tablero.columna_valida(columna)):
                print( "Columna invalida \n" )
                continue
            
            if tablero.columna_valida(columna):
                fila = tablero.get_fila_abierta(columna)
                tablero.colocar_pieza(fila, columna, 1)

                if tablero.movimiento_gane(1):
                    print("Humano es el ganador")
                    break
                
            turn = 2

        # Turno de la maquina
        elif turn == 2:
            print("\n\nTurno de la maquina\n")
            tablero, gane = agente.ganar(tablero)

            if gane:
                print("Maquina es la ganadora")
                break

            tablero, bloqueo = agente.bloquear(tablero)
            
            if not bloqueo:
                columnas_estrategia = agente.escoger_columnas(tablero)
                columna = agente.funcion_costo(tablero)
                fila = tablero.get_fila_abierta(columna)
                tablero.colocar_pieza(fila, columna, 1)

                if tablero.movimiento_gane(1):
                    print("Maquina es la ganadora")
                    break

                
            turn = 1
            
        tablero.print_tablero()
    print(" La partida ha finalizado ")

if opciones.maquina_maquina:

    tablero = tablero(6,7)
    agente1 = Agente(1,1,1,1,11)
    agente2 = Agente(1,1,1,1,2)
    turn = 1
    tablero.print_tablero()
    print(" Inicia el juego maquina vs maquina ")
    
    while not tablero.tablero_lleno():
        
        # Turno del Agente 1
        if turn == 1:
            print("\n\nTurno de la maquina #1\n")
            tablero, gane = agente1.ganar(tablero)

            if gane:
                print("Maquina #1 es la ganadora")
                break

            tablero, bloqueo = agente1.bloquear(tablero)
            if not bloqueo:
                columnas_estrategia = agente.escoger_columnas(tablero)
                columna = agente1.funcion_costo(tablero)
                fila = tablero.get_fila_abierta(columna)
                tablero.colocar_pieza(fila, columna, 1)

                if tablero.movimiento_gane(1):
                    print("Maquina #1 es la ganadora")
                    break

                
            turn = 2

        # Turno del Agente 2
        elif turn == 2:
            print("\n\nTurno de la maquina #2\n")
            tablero, gane = agente2.ganar(tablero)

            if gane:
                print("Maquina #2 es la ganadora")
                break

            tablero, bloqueo = agente2.bloquear(tablero)
            
            if not bloqueo:
                columnas_estrategia = agente2.escoger_columnas(tablero)
                columna = agente.funcion_costo(tablero)
                fila = tablero.get_fila_abierta(columna)
                tablero.colocar_pieza(fila, columna, 1)

                if tablero.movimiento_gane(1):
                    print("Maquina #2 es la ganadora")
                    break

                
            turn = 1
        continuar = input("presione ENTER para continuar")
        
        tablero.print_tablero()
    print(" La partida ha finalizado ")


'''
class Juego:

    def __init__(self):
        self.tablero = Tablero(6,7)
        self.agente1 = Agente(1,1,1,1,1)
        self.agente2 = Agente(1,1,1,1,2)

    def jugar(self):
        self.tablero.colocar_pieza(0,1,1)
        lista = self.agente1.escoger_columnas(self.tablero, 1)
        self.tablero.print_tablero()
'''
    
