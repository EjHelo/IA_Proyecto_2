import numpy as np

class Tablero:
    def __init__(self, row_count, column_count):
        self.fila = row_count
        self.columna = column_count

    def crear_tablero(self):
        self.board = np.zeros((self.fila, self.columna))

    def print_tablero(self):
        print(np.flip(self.board,0))

    def columna_valida(self,columna):
        return self.board[5][columna]==0

    def colocar_pieza(self, fila, columna, pieza):
        self.board[fila][columna]=pieza

    def get_fila_abierta(self,columna):
        for row in range (self.fila):
            if self.board[row][columna]==0:
                return row
            
def jugar():
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    tablero.print_tablero()
    
    while(True):
        column = int(input("Player 1 make your selection (0 -6): "))
        if(tablero.columna_valida(column)):
            fila = tablero.get_fila_abierta(column)
            tablero.colocar_pieza( fila, column, 1)
        tablero.print_tablero()
