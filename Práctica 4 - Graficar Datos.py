import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Práctica 4 - Graficar
def Práctica_4():

    plt.style.use('dark_background')

    #Gráfica 1
    df = pd.read_csv("csv_operacion/csv_operacion1.csv")
    x = df['Año']
    y = df['Comité']
    plt.figure(figsize=(8,5))
    plt.xlabel('Año', fontsize=15)
    plt.ylabel('Atletas', fontsize=15)
    plt.scatter(x, y)
    plt.plot(x, y, label = "Atletas")
    plt.title("Atletas por Año")    
    plt.legend()
    plt.savefig("img/Grafica1 - Atletas por Año.png")
    plt.show()
    
    #Gráfica 2
    df = pd.read_csv("csv_operacion/csv_operacion2.csv")
    x = df['Sexo']
    y = df['Nombre']
    plt.figure(figsize=(8,5))
    plt.xlabel('Sexo', fontsize=15)
    plt.ylabel('Atletas', fontsize=15)
    plt.bar(x, y, label = "Atletas")
    plt.title("Comparación entre el Sexo de los Atletas")    
    plt.legend()
    plt.savefig("img/Grafica2 - Participantes por Sexo.png")
    plt.show()
    
    #Gráfica 3
    df = pd.read_csv("csv_operacion/csv_operacion3.csv")
    x = df['Comité']
    y = df['Medalla']
    plt.figure(figsize=(8,5))
    plt.pie(y, labels=x)
    plt.title("Distribución de Medallas entre Países Participantes")
    plt.savefig("img/Grafica3 - Medallas por Comité(Total).png")
    plt.show()

    #Gráfica 4
    df = pd.read_csv("csv_operacion/csv_operacion4.csv")
    x = df['Año']
    y = df['Estatura']
    plt.figure(figsize=(8,5))
    plt.xlabel('Año', fontsize=15)
    plt.ylabel('Estatura', fontsize=15)
    plt.scatter(x, y, label="Estatura")
    plt.title("Estatura Promedio")
    plt.legend()
    plt.savefig("img/Grafica4 - Estatura promedio por sexo.png")
    plt.show()    

Práctica_4()