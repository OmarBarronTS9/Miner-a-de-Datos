import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as ols

#Atletas por año
def Práctica_6():

    plt.style.use('dark_background')
    
    df = pd.read_csv("csv_operacion/csv_operacion1.csv")
    labels = df["Comité"]
    features = df["Año"]

    slope, intercept, r, p, std_err = stats.linregress(features, labels)

    def lineFunc(x):
        return slope * x + intercept

    lineY = list(map(lineFunc, features))
    print(lineY)

    plt.figure(figsize=(8,5))
    plt.ylabel('Atletas', fontsize=15)
    plt.xlabel('Año', fontsize=15)    
    plt.scatter(features, labels, c="gray", label="Atletas Totales")
    plt.plot(features, lineY, c="red", label="Regresión")
    #plt.scatter(df, x_vars=['Temporada', 'Año'], y_vars='Sexo', size=7, aspect=0.8,kind = 'reg')
    plt.title("Atletas por Año")
    plt.legend()
    plt.savefig("img/Regresión Lineal.png")
    plt.show()    

Práctica_6()