import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

plt.style.use('dark_background')
data = pd.read_csv("csv_operacion6.csv")

X = data[["Edad", "Peso"]]
plt.scatter(X["Edad"], X["Peso"], c="gray", label='Peso')
plt.xlabel("Edad")
plt.ylabel("Peso")
plt.title("La Edad en Relación con el Peso de los Atletas")
plt.legend()
plt.savefig("img/Clustering - 0.png")
plt.show()

K=3
 
Centroids = (X.sample(n=K))
plt.scatter(X["Edad"], X["Peso"], c="gray", label='Peso')
plt.scatter(Centroids["Edad"], Centroids["Peso"], c="red", label='Puntos K')
plt.xlabel("Edad")
plt.ylabel("Peso")
plt.title("Gráfica con puntos K")
plt.legend()
plt.savefig("img/Clustering - Con puntos K.png")
plt.show()

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1, row_c in Centroids.iterrows():
        ED=[]
        for index2, row_d in XD.iterrows():
            d1 = (row_c["Edad"]-row_d["Edad"])**2
            d2 = (row_c["Peso"]-row_d["Peso"])**2
            d = sqrt(d1+d2)
            ED.append(d)
        X[i] = ED
        i = i+1
    
    C = []
    for index, row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos = i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["Peso", "Edad"]]
    if j == 0:
        diff = 1
        j = j+1
    else:
        diff = (Centroids_new['Peso'] - Centroids['Peso']).sum() + (Centroids_new['Edad'] - Centroids['Edad']).sum()
        #print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["Peso","Edad"]]

color=['gray','yellow','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    if k == 0:
        plt.scatter(data["Edad"],data["Peso"],c=color[k], label='Peso1')
    elif k == 1:
        plt.scatter(data["Edad"],data["Peso"],c=color[k], label='Peso2')
    elif k == 2:
        plt.scatter(data["Edad"],data["Peso"],c=color[k], label='Peso3')
    
plt.scatter(Centroids["Edad"],Centroids["Peso"],c='red', label='Puntos K')
plt.xlabel('Edad')
plt.ylabel('Peso')
plt.title("Clustering")
plt.legend()
plt.savefig("img/Clustering.png")
plt.show()