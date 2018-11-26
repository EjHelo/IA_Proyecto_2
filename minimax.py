import random

from tablero import Tablero

class Minimax(object):
      
    board = None
    vector = []
    
    def __init__(self, board, vector):
        self.board = board.get_tablero() #Respaldo del tablero
        self.vector = vector
    
    #Función que retorna el número de columnaa del mejor movimiento       
    def mejor_movimiento(self, obj_tablero, jugador_actual):

        tablero = []
        profundidad = 3
        for i in range(6):
            tablero += [obj_tablero.extraer_fila_completa(i)]
                
        # determinar jugadores
        if jugador_actual == 1:
            jugador_oponente = 2
        else:
            jugador_oponente = 1
        
        movimientos_permitidos = {} # enum de todos los movimientos permitidos
        for columna in range(len(self.vector)):
            # verifica si la columna tiene espacios disponibles
            col = self.vector[columna]
            if tablero[5][col] == 0:
                # Hace el movimiento en la columna para el jugador actual
                temporal = self.mover(tablero, col, jugador_actual)
                movimientos_permitidos[col] = -self.busqueda(profundidad-1, temporal, jugador_oponente)
        
        mejor_alpha = -99999999
        mejor_movimiento = None
        movimientos = movimientos_permitidos.items()
        random.shuffle(list(movimientos))
        lista_posiciones =[]
        for movimiento, alpha in movimientos:
            lista_posiciones += [[movimiento, alpha]]
            if alpha >= mejor_alpha:
                mejor_alpha = alpha
                mejor_movimiento = movimiento      
        bandera = 0
        numero_alpha = lista_posiciones[0][1]
        for i in range(len(lista_posiciones)):
            if lista_posiciones[i][1] == numero_alpha:
                bandera = 1
            else:
                bandera = 0
                break
        if bandera == 0:
            return mejor_movimiento
        else:
            indice = (len(lista_posiciones) // 2)
            return lista_posiciones[indice][0]
        
    #Funcion que retorna el valor alpha buscado en el arbol de profundidad
    def busqueda(self, profundidad, tablero, jugador_actual):
        movimientos_permitidos = [] #Todos los movimientos permitidos del tablero
        for columna in range(len(self.vector)):
            col = self.vector[columna]
            if tablero[5][col] == 0:
                temporal = self.mover(tablero, col, jugador_actual) #mueve en columna i
                movimientos_permitidos.append(temporal)
        
        if profundidad == 0 or len(movimientos_permitidos) == 0 or self.terminado(tablero):
            # retorna el valor heurístico del nodo
            return self.valor_nodo(tablero, jugador_actual)
        
        # determinar jugadores
        if jugador_actual == 1:
            jugador_oponente = 2
        else:
            jugador_oponente = 1

        alpha = -99999999
        for movimiento in movimientos_permitidos:
            if movimiento == None:
                print("Búsqueda vacía")
            alpha = max(alpha, -self.busqueda(profundidad-1, movimiento, jugador_oponente))
        return alpha
     
    #Verifica si ya hay un gana con el consecutivo de 4 fichas
    def terminado(self, tablero):
        if self.chequeo_consecutivos(tablero, 1, 4) >= 1:
            return True
        elif self.chequeo_consecutivos(tablero, 2, 4) >= 1:
            return True
        else:
            return False
    
    #Retorna un temporal del nuevo tablero con el movimiento hecho
    def mover(self, tablero, columna, jugador_actual):
                
        temporal = [x[:] for x in tablero]
        for i in range(6):
            if temporal[i][columna] == 0:
                temporal[i][columna] = jugador_actual
                return temporal

    #Heuristico que evalúa el consecutivo de fichas del tablero
    def valor_nodo(self, tablero, jugador_actual):
        
        if jugador_actual == 1:
            jugador_oponente = 2
        else:
            jugador_oponente = 1
        
        consecutivo4_actual = self.chequeo_consecutivos(tablero, jugador_actual, 4)
        consecutivo3_actual = self.chequeo_consecutivos(tablero, jugador_actual, 3)
        consecutivo2_actual = self.chequeo_consecutivos(tablero, jugador_actual, 2)
        consecutivo4_oponente = self.chequeo_consecutivos(tablero, jugador_oponente, 4)
        if consecutivo4_oponente > 0:
            return -100000
        else:
            return consecutivo4_actual*100000 + consecutivo3_actual*100 + consecutivo2_actual
            
    def chequeo_consecutivos(self, tablero, jugador_actual, consecutivo):
        contador = 0
        for i in range(6): 
            for columna in range(len(self.vector)):
                j = self.vector[columna]
                if tablero[i][j] == jugador_actual:
                    # chequea si un consecutivo vertical empieza en (i, j)
                    contador += self.vertical_horizontal_consecutivo(i, j, tablero, consecutivo, "vertical")
                    # chequea si un consecutivo horizontal empieza en (i, j)
                    contador += self.vertical_horizontal_consecutivo(i, j, tablero, consecutivo, "Horizontal")
                    # chequea si una diagonal empieza en (i, j)
                    contador += self.diagonal_consecutivo(i, j, tablero, consecutivo)
        # retorna la suma de consecutivos 
        return contador
            
    def vertical_horizontal_consecutivo(self, row, col, tablero, consecutivo, modo):
        contador = 0
        if modo == "vertical": 
            for i in range(row, 6):
                if tablero[i][col] == tablero[row][col]:
                    contador += 1
                else:
                    break
        else:
            for columna in range(len(self.vector)):
                j = self.vector[columna]
                if tablero[row][j] == tablero[row][col]:
                    contador += 1
                else:
                    break
    
        if contador >= consecutivo:
            return 1
        else:
            return 0
    
    
    def diagonal_consecutivo(self, row, col, tablero, consecutivo):

        total = 0
        # chequeo diagonals pendiente positiva
        contador = 0
        j = col
        for i in range(row, 6):
            if j > 6:
                break
            elif tablero[i][j] == tablero[row][col]:
                contador += 1
            else:
                break
            j += 1 # incrementa columna cuando fila es incrementada
            
        if contador >= consecutivo:
            total += 1

        # chequeo diagonals pendiente negativa
        contador = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif tablero[i][j] == tablero[row][col]:
                contador += 1
            else:
                break
            j += 1 # incrementa columna cuando fila es incrementada

        if contador >= consecutivo:
            total += 1

        return total

#m = Minimax(tablero, [0,1,2,3,4,5,6])

#print(m.mejor_movimiento(tablero, 1))
