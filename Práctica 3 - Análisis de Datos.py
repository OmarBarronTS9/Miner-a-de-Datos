from itertools import groupby
import pandas as pd
import numpy as np
import random

#Práctica 3 - Realizar análisis de datos
def Práctica_3():

    file_name = "csv_limpio.csv"

    #1. Contar el número de atletas por comités que participaron por año
    df1 = pd.read_csv(file_name)
    df_C = df1.groupby(["Año"])[['Comité']].count()
    df_C.reset_index(inplace  = True)
    df_C.set_index("Año", inplace = True)
    df_C.to_csv('csv_operacion1.csv')

    #2. Contar atletas por su sexo
    df2 = pd.read_csv(file_name)
    df_A = df2.groupby(["Sexo"])[['Nombre']].count()
    df_A.reset_index(inplace  = True)
    df_A.set_index("Sexo", inplace = True)
    df_A.to_csv('csv_operacion2.csv')    

    #3. Contar las medallas por comité en la historia
    df3 = pd.read_csv(file_name)
    df_M = df3.groupby(["Comité"])[['Medalla']].count()
    df_M.reset_index(inplace  = True)   
    df_M.set_index("Comité", inplace = True)
    df_M.to_csv('csv_operacion3.csv')        

    #4. El promedio de estatura entre sexo, por año
    df4 = pd.read_csv(file_name)
    df_S = df4.groupby(["Año", "Sexo"])[['Estatura']].mean()
    df_S.reset_index(inplace  = True)
    df_S.set_index("Año", inplace = True)        
    df_S.to_csv('csv_operacion4.csv')   

    #5. Eliminar columnas para realizar operaciones con la edad y el peso para data classification
    df5 = pd.read_csv(file_name) 
    df5 = df5[df5['Edad'].notna()]
    df5 = df5[df5['Peso'].notna()]
    df5 = df5[df5['Año'].notna()]
    df_E = df5.groupby(["Año", "Edad"])[['Peso']].mean()
    df_E.reset_index(inplace  = True)
    df_E.set_index("Año", inplace = True)         
    df_E.to_csv('csv_operacion6.csv')  

    # df5 = pd.read_csv("csv_limpio.csv") 
    # df5 = df5.drop(['ID', 'Nombre', 'Sexo', 'Estatura', 'Equipo', 'Comité', 'Año', 'Temporada', 'Ciudad', 'Deporte', 'Evento', 'Medalla'], axis=1)
    # df5 = df5[df5['Edad'].notna()]
    # df5 = df5[df5['Peso'].notna()]
    # df5.reset_index(inplace  = True)
    # df5.set_index("Edad", inplace = True)       
    # df5.to_csv('csv_operacion6.csv')      

Práctica_3()