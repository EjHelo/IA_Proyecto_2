from algoritmo_genetico import AlgoritmoGenetico
from agente import Agente
from tablero import Tablero

def test_num_gen():
    algoritmo = AlgoritmoGenetico(4,2,2)
    assert algoritmo.num_gen == 2

def test_inicio_poblacion():
    algoritmo = AlgoritmoGenetico(4,2,2)
    tam_poblacion = algoritmo.get_poblacion()
    assert len(tam_poblacion) == 4

def test_cruce_agente():
    agente1 = Agente(1,1,1,1,1)
    agente2 = Agente(0,0,0,0,2)
    algoritmo = AlgoritmoGenetico(2,1,2)
    nuevo_agente = algoritmo.cruce_agentes_aux(agente1,agente2)
    assert nuevo_agente.get_estrategias() == [1,0,1,0]

def test_mutacion_agente():
    algoritmo = AlgoritmoGenetico(1,1,2)
    agente = Agente(1,1,1,1,1)
    poblacion = [agente]
    nuevo_agente = algoritmo.mutacion_agente(poblacion)
    estrat_agente_viejo = agente.get_estrategias()
    estrat_agente_nuevo = nuevo_agente.get_estrategias()
    count = 0
    for i in range (len(agente.get_estrategias())):
        if estrat_agente_viejo[i]!=estrat_agente_nuevo[i]:
            count+=1
    assert count == 1
    
