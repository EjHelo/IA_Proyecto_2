
from minimax import *
from tablero import *


def test_busqueda():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		    [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1], 
    		    [0.0, 2.0, 2.0, 0.0, 0.0, 2, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]


    profundidad = 0
    jugador_actual = 2
    #Ejecución
    resultado = m.busqueda(profundidad, tablero, jugador_actual)
    #Aserión
    assert resultado == 2

def test_terminado():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		   [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    		   [0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    #Ejecución
    resultado = m.terminado(tablero)
    #Aserión
    assert resultado == False

def test_mover():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    			 [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    			 [0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 1], 
    			 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    			 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    			 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    columna = 5
    jugador_actual = 2
    #Ejecución
    resultado = m.mover(tablero, columna, jugador_actual)
    #Aserión
    assert resultado == [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    					 [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    					 [0.0, 2.0, 2.0, 0.0, 0.0, 2, 1], 
    					 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    					 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    					 [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

def test_valor_nodo():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		    [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1], 
    		    [0.0, 2.0, 2.0, 0.0, 0.0, 2, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]


    jugador_actual = 2
    #Ejecución
    resultado = m.valor_nodo(tablero, jugador_actual)
    #Aserión
    assert resultado == 2

def test_chequeo_consecutivos():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [ [1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1],
    		    [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 0.0], 
    			[0.0, 2.0, 2.0, 0.0, 1, 2, 0.0], 
    			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    			[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
    jugador_actual = 2
    consecutivo = 2
    #Ejecución
    resultado = m.chequeo_consecutivos(tablero, jugador_actual, consecutivo)
    #Aserión
    assert resultado == 2

def test_chequeo_consecutivos_1():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		   [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    		   [0.0, 2.0, 2.0, 0.0, 0.0, 1, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    jugador_actual = 2
    consecutivo = 3
    #Ejecución
    resultado = m.chequeo_consecutivos(tablero, jugador_actual, consecutivo)
    #Aserión
    assert resultado == 0

def test_vertical_horizontal_consecutivo():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		   [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    		   [0.0, 2.0, 2.0, 0.0, 0.0, 1, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    row = 1
    col = 5
    consecutivo = 4
    modo = "vertical"
    #Ejecución
    resultado = m.vertical_horizontal_consecutivo(row, col, tablero, consecutivo, modo)
    #Aserión
    assert resultado == 0

def test_vertical_horizontal_consecutivo_1():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		   [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    		   [0.0, 2.0, 2.0, 0.0, 0.0, 1, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    row = 1
    col = 6
    consecutivo = 2
    modo = "horizontal"
    #Ejecución
    resultado = m.vertical_horizontal_consecutivo(row, col, tablero, consecutivo, modo)
    #Aserión
    assert resultado == 0

def test_diagonal_consecutivo():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    m = Minimax(tablero, [4,5,6])
    tablero = [[1.0, 1.0, 2.0, 1.0, 2.0, 1.0, 1], 
    		   [2.0, 1.0, 1.0, 2.0, 2.0, 1.0, 2], 
    		   [0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 1], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    		   [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    row = 0
    col = 6
    consecutivo = 4
    #Ejecución
    resultado = m.diagonal_consecutivo(row, col, tablero, consecutivo)
    #Aserión
    assert resultado == 0

