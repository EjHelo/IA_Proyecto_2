
from agente import Agente
from tablero import Tablero

def test_get_estrategias():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    #Ejecución
    resultado = agente.get_estrategias()
    #Aserión
    assert resultado == [1,1,1,1]


def test_set_victorias():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    #Ejecución
    agente.set_victorias(5)
    resultado = agente.get_victorias()
    #Aserión
    assert resultado == 5

def test_set_pieza():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    #Ejecución
    agente.set_pieza(1)
    resultado = agente.get_pieza()
    #Aserión
    assert resultado == 1

def test_ganar():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    tablero = Tablero(6,7)
    tablero.crear_tablero()
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

    #Ejecución
    resultado1, resultado2 = agente.ganar(tablero)
    tablero.colocar_pieza(1,5,2)

    #Aserión
    assert (resultado1.board).tolist() == (tablero.board).tolist()
    assert resultado2 == True

def test_bloquear():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    tablero = Tablero(6,7)
    tablero.crear_tablero()
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

    #Ejecución
    resultado1, resultado2 = agente.bloquear(tablero)

    #Aserión
    assert (resultado1.board).tolist() == (tablero.board).tolist()
    assert resultado2 == False

def test_escoger_columnas():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    tablero = Tablero(6,7)
    tablero.crear_tablero()
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

    #Ejecución
    resultado = agente.escoger_columnas(tablero)

    #Aserión
    assert resultado == [1,2,3,4,5]

def test_eliminar_repetidos():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    centro = [2,3,4]
    secuencia = [5,1,2,3,4,5]
    fila = [5]
    par = [1,3,5]
    #Ejecución
    resultado = agente.eliminar_repetidos(centro,secuencia,fila,par)
    #Aserión
    assert resultado == [1,2,3,4,5]

def test_funcion_costo():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    tablero = Tablero(6,7)
    tablero.crear_tablero()
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

    columnas = [1,2,3,4,5]

    #Ejecución
    resultado = agente.funcion_costo(tablero, columnas)

    #Aserión
    assert resultado == 4

def test_validar_columnas():
	#Datos de entrada
    agente = Agente(1,1,1,1,2)
    tablero = Tablero(6,7)
    tablero.crear_tablero()
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

    columnas = [1,2,4,5]

    #Ejecución
    resultado = agente.validar_columnas(tablero, columnas)

    #Aserión
    assert resultado == [1,2,4,5]
