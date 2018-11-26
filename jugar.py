from agente import Agente
from tablero import Tablero
class Jugar:

    def __init__(self, agente1, agente2):
        self.tablero = Tablero(6,7)
        self.agente1 = agente1
        self.agente2 = agente2
        self.turn =1

    def jugar(self):
        flag_tie = True
        print("pase")
        while not self.tablero.tablero_lleno():
           
        # Turno del Agente 1
            if self.turn == 1:
                print("\n\nTurno de la maquina #1\n")
                self.tablero, gane = self.agente1.ganar(self.tablero)

                if gane:
                    print("Maquina #1 es la ganadora")
                    break

                self.tablero, bloqueo = self.agente1.bloquear(self.tablero)
                if not bloqueo:
                    columnas_estrategia = self.agente1.escoger_columnas(self.tablero)
                    columna = self.agente1.funcion_costo(self.tablero, columnas_estrategia)
                    fila = self.tablero.get_fila_abierta(columna)
                    self.tablero.colocar_pieza(fila, columna, 1)

                    if self.tablero.movimiento_gane(1):
                        print("Maquina #1 es la ganadora")
                        self.agente1.incrementar_victorias()
                        flag_tie = True
                        break

                    
                self.turn = 2

            # Turno del Agente 2
            elif self.turn == 2:
                print("\n\nTurno de la maquina #2\n")
                self.tablero, gane = self.agente2.ganar(self.tablero)

                if gane:
                    print("Maquina #2 es la ganadora")
                    break

                self.tablero, bloqueo = self.agente2.bloquear(self.tablero)
                
                if not bloqueo:
                    columnas_estrategia = self.agente2.escoger_columnas(self.tablero)
                    columna = self.agente2.funcion_costo(self.tablero, columnas_estrategia)
                    fila = self.tablero.get_fila_abierta(columna)
                    self.tablero.colocar_pieza(fila, columna, 2)

                    if self.tablero.movimiento_gane(2):
                        print("Maquina #2 es la ganadora")
                        self.agente2.incrementar_victorias()
                        flag_tie=True
                        break

                    
                self.turn = 1
        if(flag_tie):
            self.agente1.incrementar_victorias()
            self.agente2.incrementar_victorias()
        self.tablero.print_tablero()
        print(" La partida ha finalizado ")
        return self.agente1, self.agente2
