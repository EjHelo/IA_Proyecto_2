import numpy as np

class Tablero:
    
    #Constructor
    def __init__(self, row_count, column_count):
        self.fila = row_count
        self.columna = column_count
        self.crear_tablero()


    def get_columna(self):
        return self.columna


    def get_fila(self):
        return self.fila

    
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
        for fila in range (self.fila):
            if self.board[fila][columna]==0:
                return fila


    def get_lista_columna(self, pieza):
        lista = []
        for fila in range (self.fila):
            for c in range (self.columna):
                if self.board[fila][c]==0:
                    if self.revisar_columna(fila,c,pieza):
                        lista+=[c]
        return lista


    def revisar_columna(self,fila,columna,pieza):
        if fila != 0:
            if self.board[fila-1][columna]==pieza:
                return True


    def get_lista_fila(self, pieza):
        lista = []
        for fila in range (self.fila):
            for c in range (self.columna):
                if self.board[fila][c]==0:
                    if self.revisar_fila(fila,c,pieza):
                        lista+=[c]
        return lista


    def revisar_fila(self,fila,columna,pieza):
        if columna == 0:
            if self.board[fila][columna+1]==pieza:
                return True
        elif columna ==6:
            if self.board[fila][columna-1]==pieza:
                return True
        else:
            if self.board[fila][columna+1]==pieza or self.board[fila][columna-1]==pieza:
                return True

    def get_lista_espacio(self,pieza):
        lista=[]
        for fila in range (self.fila-1):
            for c in range (self.columna-1):
                if self.board[fila][c]== pieza:
                    if (self.revisar_espacio(fila,c,pieza))!=0:
                        print("entre")
                        lista+=[c+self.revisar_espacio(fila,c,pieza)]
                    
        return lista

    def get_lista_secuencia(self,pieza):
        lista=[]
        for fila in range (self.fila-1):
            for c in range (self.columna-1):
                if self.board[fila][c] == 0:
                    if(self.revisar_secuencia(fila,c,pieza)):
                        lista+=[c]
        return lista


    def movimiento_gane(self,pieza):
    # Gana horizontal
        for col in range(self.columna-3):
            for fila in range(self.fila):
                if self.board[fila][col] == piece and self.board[fila][col+1] == piece and self.board[fila][col+2] == piece and self.board[fila][col+3] == piece :
                    return True

    # Gana vertical
        for col in range(self.columna):
            for fila in range(self.fila-3):
                if self.board[fila][col] == piece and self.board[fila+1][col] == piece and self.board[fila+2][col] == piece and self.board[fila+3][col] == piece :
                    return True

    # Gana por diagonal
        for col in range(self.columna-3):
            for fila in range(self.fila-3):
                if self.board[fila][col] == piece and self.board[fila+1][col+1] == piece and self.board[fila+2][col+2] == piece and self.board[fila+3][col+3] == piece :
                    return True
                
            for fila in range(3, self.fila):
                if self.board[fila][col] == piece and self.board[fila-1][col+1] == piece and self.board[fila-2][col+2] == piece and self.board[fila-3][col+3] == piece :
                    return True
        return False

    #Verifica si el tablero está lleno
    def tablero_lleno(self):
        if not 0 in self.board:
            return True
        return False
    
    def revisar_espacio(self, fila, columna, pieza):
        if columna == 0 or columna ==1:
            if (self.get_fila_abierta(columna+1)==self.get_fila_abierta(columna+2)):
                if(self.board[fila][columna+1]==0 and self.board[fila][columna+2]==0):
                    return 2
        elif columna == 5 or columna == 6:
            if (self.get_fila_abierta(columna-1) == self.get_fila_abierta(columna-2)):
                if(self.board[fila][columna-1]==0 and self.board[fila][columna-2]==0):
                    return -2
        else:
            if (self.get_fila_abierta(columna+1)==self.get_fila_abierta(columna+2)):
                if(self.board[fila][columna+1]==0 and self.board[fila][columna+2]==0):
                    return 2
            elif (self.get_fila_abierta(columna-1) == self.get_fila_abierta(columna-2)):
                if(self.board[fila][columna-1]==0 and self.board[fila][columna-2]==0):
                    return -2
        return 0


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
        lista = tablero.get_lista_columna(1)
        print(lista)
