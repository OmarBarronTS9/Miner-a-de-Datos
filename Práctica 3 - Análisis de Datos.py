from itertools import groupby
import pandas as pd
import numpy as np
import random

#Práctica 3 - Realizar análisis de datos
def Práctica_3():

    file_name = "csv_operacion/csv_limpio.csv"

    #1. Contar el número de atletas por comités que participaron por año
    df1 = pd.read_csv(file_name)
    df_C = df1.groupby(["Año"])[['Comité']].count()
    df_C.reset_index(inplace  = True)
    df_C.set_index("Año", inplace = True)
    df_C.to_csv('csv_operacion/csv_operacion1.csv')

    #2. Contar atletas por su sexo
    df2 = pd.read_csv(file_name)
    df_A = df2.groupby(["Sexo"])[['Nombre']].count()
    df_A.reset_index(inplace  = True)
    df_A.set_index("Sexo", inplace = True)
    df_A.to_csv('csv_operacion/csv_operacion2.csv')    

    #3. Contar las medallas por comité en la historia
    df3 = pd.read_csv(file_name)
    df_M = df3.groupby(["Comité"])[['Medalla']].count()
    df_M.reset_index(inplace  = True)   
    df_M.set_index("Comité", inplace = True)
    df_M.to_csv('csv_operacion/csv_operacion3.csv')        

    #4. El promedio de estatura entre sexo, por año
    df4 = pd.read_csv(file_name)
    df_S = df4.groupby(["Año", "Sexo"])[['Estatura']].mean()
    df_S.reset_index(inplace  = True)
    df_S.set_index("Año", inplace = True)        
    df_S.to_csv('csv_operacion/csv_operacion4.csv')   

    #5. Eliminar columnas para realizar operaciones con la edad y el peso para data classification
    df5 = pd.read_csv(file_name) 
    df5 = df5[df5['Edad'].notna()]
    df5 = df5[df5['Peso'].notna()]
    df5 = df5[df5['Año'].notna()]
    df_E = df5.groupby(["Año", "Edad"])[['Peso']].mean()
    df_E.reset_index(inplace  = True)
    df_E.set_index("Año", inplace = True)         
    df_E.to_csv('csv_operacion/csv_operacion6.csv')  

    #6. Agrupar Medallas, Año y Contar los atletas con el sexo     
    df6 = pd.read_csv(file_name) 
    df6 = df6[df6['Medalla'].notna()]
    df_F = df6.groupby(["Año", "Medalla"])[['Sexo']].count()
    df_F.reset_index(inplace  = True)
    df_F.set_index("Año", inplace = True) 
    df_F.to_csv('csv_operacion/csv_operacion7.csv')

Práctica_3()