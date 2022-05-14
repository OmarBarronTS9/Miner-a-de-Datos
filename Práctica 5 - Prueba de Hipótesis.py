import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import fisher_exact
import statsmodels.api as sm
import statsmodels.formula.api as ols

#Hipótesis: cuando los juegos son en invierno participan menos atletas que en verano
def Práctica_5():

    plt.style.use('dark_background')
    
    df = pd.read_csv("csv_operacion/csv_limpio.csv")
    df_T = df.groupby(["Temporada", "Año"])[['Sexo']].count()
    df_T.reset_index(inplace = True)
    df_T.set_index("Temporada", inplace = True)
    df_T.to_csv('csv_operacion/csv_operacion5.csv') 

    df = pd.read_csv("csv_operacion/csv_operacion5.csv")
    x = df['Temporada']
    y = df['Sexo']
    plt.figure(figsize=(8,5))
    plt.xlabel('Temporada', fontsize=15)
    plt.ylabel('Atletas', fontsize=15)
    plt.bar(x, y, label="Atletas")
    plt.title("Hipótesis - Participan mas Atletas en los Juegos de Verano que en Invierno")
    plt.legend()
    plt.savefig("img/Comprobación de Hipótesis.png")
    plt.show()    

Práctica_5()