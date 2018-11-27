from agente import Agente
from tablero import Tablero
from jugar import Jugar
import random as rd
from copy import deepcopy

#Debe tener un N - n agentes
#Debe tener un G - g generaciones
#fitness = total de victorias

class AlgoritmoGenetico:
    poblacion = []
    
    '''Constructor'''
    def __init__(self, tam_poblacion, numero_agentes, numero_generaciones):
        self.poblacion=[]
        self.iniciar_poblacion(tam_poblacion)
        self.num_agentes = numero_agentes
        self.num_gen = numero_generaciones
        self.resultado = ""
        
    ''' Inicializacion de la poblacion'''
    def iniciar_poblacion(self, tam):
        for i in range(tam):
            probabilidad  = self.get_random_caracteristica()
            agente = Agente(probabilidad[0], probabilidad[1], probabilidad[2],probabilidad[3],1)
            self.poblacion+=[agente]

    '''setter y getter'''
    def get_poblacion(self):
        return self.poblacion
    def set_poblacion(self,poblacion):
        self.poblacion = poblacion

    '''aleatoriedad de probabilidades para las caracteristicas'''
    def get_random_caracteristica(self):
        lista = []
        for i in range(4):
            probabilidad = round(rd.random(),2)
            lista.append(probabilidad)
        return lista
    
    ''' Realizacion del juego entre agentes '''
    def juego_genetico(self):

        temporal = self.poblacion[:]
        for i in range (len(temporal)):
            for j in range (len(temporal)):
                if i!=j:
                    temporal[i], temporal[j] = self.jugar(temporal[i],temporal[j])

        self.poblacion = sorted(temporal[:]  , key=lambda objeto:objeto.victorias, reverse=True)
  

    ''' cada generacion se realiza el juego_genetico'''
    def generaciones(self):
        for i in range (self.num_gen):
            self.juego_genetico()
            self.anotar_resultados(i)
            self.cruce_agentes()
            self.reset_victorias()
        poblacion_ordenada = sorted(self.poblacion, key=lambda objeto: objeto.victorias, reverse=True)

        print(self.resultado)
        print("Mejor configuracion")
        poblacion_ordenada[0].estrategias_to_string()

    def reset_victorias(self):
        for agente in self.poblacion:
            agente.set_victorias(0)
        
    def anotar_resultados(self, gen):
        self.resultado+=" == Generacion ==" + str(gen) +"\n"
        for agente in self.poblacion:
            config = "              "+str(agente.get_estrategias())+"====== Victorias= "+str(agente.get_victorias())+"\n"
            self.resultado += config
        self.resultado+=" ========= \n"

        
    ''' determinacion del ganador'''
    def jugar(self,agente1, agente2):
        
        agente1.set_pieza(1)
        agente2.set_pieza(2)
        juego = Jugar(agente1,agente2)
        return juego.jugar()
     
    '''estrategias de cada agente de la poblacion '''
    def print_estrategias(self):
        for a in self.poblacion:
            print(a.get_estrategias())


    ''' cruce de agentes y una mutacion'''
    def cruce_agentes(self):

        poblacion_ordenada = sorted(self.poblacion, key=lambda objeto: objeto.victorias, reverse=True)
        nueva_poblacion=poblacion_ordenada[:self.num_agentes]
        resto_poblacion=poblacion_ordenada[self.num_agentes:]
        resultado = []
        resultado += nueva_poblacion
        for i in range (len(resto_poblacion)):
            
            if( i==len(resto_poblacion)-1):
                agente = self.mutacion_agente(nueva_poblacion)
                resultado+=[agente]
                break;
                
            else:
                agente = self.cruce_agentes_aux(poblacion_ordenada[i],poblacion_ordenada[i+1])
                resultado.append(agente)
        self.poblacion = resultado[:]
        
    def cruce_agentes_aux(self, agente1, agente2):
        estrategias1 = agente1.get_estrategias()
        estrategias2 = agente2.get_estrategias()
        nuevo_agente = Agente(estrategias1[0],estrategias2[1], estrategias1[2],estrategias2[3],1)
        return nuevo_agente

    def mutacion_agente(self, poblacion):
        largo = len(poblacion)
        indice = rd.randint(1,largo)-1
        estrategias = poblacion[indice].get_estrategias()
        probabilidad = round(rd.random(),2)
        indice_estrategia = rd.randint(1,4)-1
        estrategias[indice_estrategia] = probabilidad
        agente = Agente(estrategias[0],estrategias[1],estrategias[2],estrategias[3],1)
        return agente

    
    
