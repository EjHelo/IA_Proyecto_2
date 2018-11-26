from agente import Agente
from tablero import Tablero
import random as rd

#Debe tener un N - n agentes
#Debe tener un G - g generaciones
#fitness = total de victorias

class AlgoritmoGenetico:
    poblacion = []

    def __init__(self, tam_poblacion, configuracion, numero_agentes, numero_generaciones):
        self.iniciar_poblacion(tam_poblacion, configuracion)
        self.num_agentes = numero_agentes
        self.num_gen = numero_generaciones

    def iniciar_poblacion(self, tam, config):
        for i in range(tam):
            probabilidad  = self.get_random_caracteristica()
            agente = Agente(probabilidad[0], probabilidad[1], probabilidad[2],probabilidad[3],1)
            self.poblacion+=[agente]

    def get_random_caracteristica(self):
        lista = []
        for i in range(4):
            probabilidad = round(rd.random(),2)
            lista.append(probabilidad)
        return lista
    ''' Debe realizar juego '''
    def juego_genetico(self):
        lista=[1,2,3,4,5]
        aux = []
        res = []
        while(lista!=[]):
            aux = lista[:1]
            lista=lista[1:]
            for agente in lista:
                #victorias y se pone en resultado
                print(aux, lista)
            res+=[aux]
        print(res)

    ''' cada generacion se realiza el juego_genetico'''
    def generaciones(self):
        for g in range(self.num_gen):
            print(g)

    ''' determinacion del ganador'''
    def jugar(agente1, agente2):
        tablero = Tablero(6,7)
        
    
        

    def print_strategias(self):
        for a in self.poblacion:
            print(a.get_estrategias())
    
