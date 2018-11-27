# IA Proyecto 2

Tecnológico de Costa Rica

Ingeniería en Computación

Proyecto #2 - Inteligencia Artificial

# Manual de uso

## Instalación  de los requerimientos:
Este proyecto está desarrollado en Python versión 3.6, es importante mencionar que  NO funciona en versiones de Python inferior a 3.

Para la ejecución del sistema, es necesaria la herramienta "pip" que es un sistema de gestión de paquetes, utilizado para instalar bibliotecas para Python y modulos enviados. Una vez instalado pip se podrán instalar todas las bibliotecas necesarias para ejecutar el proyecto. Estas bibliotecas son:

* **NumPy:** Utilizado en arrays y compatibilidad con otras bibliotecas.
* **Pytest:** Utilizado para hacer las pruebas unitarias de los funciones.

## Comandos:

Para instalar las bibliotecas **(Numpy, Pytest)** se llama a un mismo comando con la diferencia en el nombre de las bibliotecas

    pip install nombre_bibloteca

 
## Uso del sistema
Después de haber instalado todas las bibliotecas necesarias para el proyecto, se debe clonar el repositorio en la computadora y abrir una termial o línea de comandos para encontrar la ubicación de los archivos y poder ejecutarlos. 

Para ejecutar los algoritmos de clasificación se debe ingresar en la línea de comandos **python main.py** seguida de diferentes banderas. 

Este programa recibe varias banderas, las cuales tienen un nombre, una descripción y un rango permitido para poder ejecutrase. Estas banderas son:

| Símbolo               	| Explicación                | Rango                                            |
|-------------------------	|--------------------------------------------------------------	|----------------------------------------------------	|
| --humano-maquina  | Ejecuta la modalidad con Humano vs. Máquina  	| True o False  |
| --maquina-maquina  | Ejecuta la modalidad con Máquina vs. Máquina  	| True o False  |
| --maquina-configuracion  | Ejecuta la configuacion de la Máquina  	| True o False  |
| --algoritmo-genetico  | Ejecuta la modalidad con Algoritmo Genético  	| True o False  |
| --cantidad-agentes  | Asigna la cantidad de agentes  	| True o False  |
| --cantidad-generaciones  | Asigna la cantidad de generaciones 	| True o False  |
| --tamaño-poblacion  | Asigna el tamaño de la población  	| True o False  |
                                                                               	



## Pruebas Unitarias

Para ejecutar las pruebas unitarias se debe ir a la línea de comandos o terminal y ejecutar el comando

    python -m pytest
    
Muestras si las pruebas son válidas o no
