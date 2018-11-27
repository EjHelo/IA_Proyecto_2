from Tablero import *

   
def test_columna_valida():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    resultado = tablero.columna_valida(1)
    #Aserión
    assert resultado == True

def test_colocar_pieza():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(2,2,2)
    resultado = tablero.board[2][2] 
    #Aserión
    assert resultado == 2

def test_get_fila_abierta():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    resultado = tablero.get_fila_abierta(3)
    #Aserión
    assert resultado == 0

def test_get_fila_abierta_1():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,2,2)
    tablero.colocar_pieza(1,2,2)
    resultado = tablero.get_fila_abierta(2)
    #Aserión
    assert resultado == 2

def test_get_lista_columna():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    tablero.colocar_pieza(0,3,2)
    tablero.colocar_pieza(0,4,2)
    resultado = tablero.get_lista_columna(1)
    #Aserión
    assert resultado == [0,1,2]

def test_revisar_columna():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    resultado = tablero.revisar_columna(1,2,1)
    #Aserión
    assert resultado == True

def test_revisar_columna_1():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,2)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    resultado = tablero.revisar_columna(1,0,2)
    #Aserión
    assert resultado == True

def test_get_lista_fila():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    tablero.colocar_pieza(0,3,2)
    tablero.colocar_pieza(0,4,2)
    resultado = tablero.get_lista_fila(1)
    #Aserión
    assert resultado == []


def test_revisar_fila():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,2)
    tablero.colocar_pieza(1,1,1)
    tablero.colocar_pieza(0,2,1)
    resultado = tablero.revisar_fila(1,0,1)
    #Aserión
    assert resultado == True

def test_get_lista_espacio():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    tablero.colocar_pieza(0,3,2)
    tablero.colocar_pieza(0,4,2)
    resultado = tablero.get_lista_espacio(2)
    #Aserión
    assert resultado == [6]

def test_get_lista_secuencia():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,1)
    tablero.colocar_pieza(0,3,2)
    tablero.colocar_pieza(0,4,2)
    resultado = tablero.get_lista_secuencia(2)
    #Aserión
    assert resultado == [5,2,3,4,5]

def test_revisar_secuencia():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,2)
    tablero.colocar_pieza(0,3,1)
    tablero.colocar_pieza(0,4,2)
    tablero.colocar_pieza(0,5,1)
    tablero.colocar_pieza(1,1,1)
    tablero.colocar_pieza(1,2,2)
    tablero.colocar_pieza(1,3,2)
    tablero.colocar_pieza(1,4,2)
    fila = 1
    columna = 2
    pieza= 2

    resultado = tablero.revisar_secuencia(fila,columna,pieza)
    #Aserión
    assert resultado == True
    
def test_revisar_espacio():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,2)
    tablero.colocar_pieza(0,3,1)
    tablero.colocar_pieza(0,4,2)
    tablero.colocar_pieza(0,5,1)
    tablero.colocar_pieza(1,1,1)
    tablero.colocar_pieza(1,2,2)
    tablero.colocar_pieza(1,3,2)
    tablero.colocar_pieza(1,4,2)
    fila = 1
    columna = 2
    pieza= 2

    resultado = tablero.revisar_espacio(fila,columna,pieza)
    #Aserión
    assert resultado == 0

def test_movimiento_gane():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,2)
    tablero.colocar_pieza(0,3,1)
    tablero.colocar_pieza(0,4,2)
    tablero.colocar_pieza(0,5,1)
    tablero.colocar_pieza(1,1,1)
    tablero.colocar_pieza(1,2,2)
    tablero.colocar_pieza(1,3,2)
    tablero.colocar_pieza(1,4,2)

    resultado = tablero.movimiento_gane(2)
    #Aserión
    assert resultado == False

def test_tablero_lleno():
    #Datos de entrada
    tablero = Tablero(6,7)
    tablero.crear_tablero()
    #Ejecución
    tablero.colocar_pieza(0,0,1)
    tablero.colocar_pieza(0,1,1)
    tablero.colocar_pieza(0,2,2)
    tablero.colocar_pieza(0,3,1)
    tablero.colocar_pieza(0,4,2)
    tablero.colocar_pieza(0,5,1)
    tablero.colocar_pieza(1,1,1)
    tablero.colocar_pieza(1,2,2)
    tablero.colocar_pieza(1,3,2)
    tablero.colocar_pieza(1,4,2)

    resultado = tablero.tablero_lleno()
    #Aserión
    assert resultado == False
    


