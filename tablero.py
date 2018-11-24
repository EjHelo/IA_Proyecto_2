import numpy as np

class Tablero:
    #Constructor
    def __init__(self, row_count, column_count):
        self.fila = row_count
        self.columna = column_count

    #creacion de tablero
    def crear_tablero(self):
        self.board = np.zeros((self.fila, self.columna))

    #imprimir tablero
    def print_tablero(self):
        print(np.flip(self.board,0))

    #verifica si la columna esta llena
    def columna_valida(self,columna):
        return self.board[5][columna]==0

    #coloca la pieza en la columna
    def colocar_pieza(self, fila, columna, pieza):
        self.board[fila][columna]=pieza

    #busca el espacio mas abajo de la columna que este desocupada
    def get_fila_abierta(self,columna):
        for row in range (self.fila):
            if self.board[row][columna]==0:
                return row

    def get_lista_secuencia(self,pieza):
        lista=[]
        for row in range (self.fila-1):
            for c in range (self.columna-1):
                if self.board[row][c] == 0:
                    if(self.revisar_secuencia(row,c,pieza)):
                        print("estoy en: \n")
                        print(row)
                        print(c)
                        lista+=[c]
        return lista

    def revisar_secuencia(self,fila, columna, pieza):
        if fila==0:
            if columna ==0:
                if (self.board[fila+1][columna]==pieza or self.board[fila][columna+1]==pieza or self.board[fila+1][columna+1]==pieza):
                    return True
            elif columna == 6:
                if (self.board[fila+1][columna]==pieza or self.board[fila][columna-1]==pieza or self.board[fila+1][columna-1]==pieza):
                    return True
            else:
                if (self.board[fila-1][columna]==pieza or self.board[fila+1][columna]==pieza or self.board[fila-1][columna+1]==pieza or self.board[fila+1][columna+1]==pieza or self.board[fila][columna-1]==pieza):
                    return True
        else:
            if columna ==0:
                if (self.board[fila+1][columna]==pieza or self.board[fila][columna+1]==pieza or self.board[fila+1][columna+1]==pieza or self.board[fila-1][columna]==pieza):
                    return True
            elif columna == 6:
                if (self.board[fila+1][columna]==pieza or self.board[fila][columna-1]==pieza or self.board[fila+1][columna-1]==pieza):
                    return True
            else:
                if (self.board[fila-1][columna]==pieza or self.board[fila+1][columna]==pieza or self.board[fila-1][columna+1]==pieza or self.board[fila+1][columna+1]==pieza or self.board[fila][columna-1]==pieza) or self.board[fila-1][columna-1]==pieza:
                    return True
        return False
    #por si ocupa obtener el talero
    def get_tablero(self):
        return self.board

    #por si ocupa reemplazar tablero
    def set_tablero(self, tablero):
        self.board = tablero

    def revisar_punto(self, fila, columna):
        if self.board[fila][columna]==1:
            print (self.board[fila][columna])
        else:
            print("nolo encontre")

#ejemplo           
def jugar():
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    tablero.print_tablero()
    jugador = 1
    while(True):
        
        column = int(input("Player 1 make your selection (0 -6): "))
        if(tablero.columna_valida(column)):
            fila = tablero.get_fila_abierta(column)
            if jugador ==1:
                tablero.colocar_pieza( fila, column, 1)
                jugador =2
            else:
                tablero.colocar_pieza(fila,column,2)
                jugador=1
        tablero.print_tablero()
        #tablero.revisar_punto(fila,column)
        lista = tablero.get_lista_secuencia(1)
        print(lista)
