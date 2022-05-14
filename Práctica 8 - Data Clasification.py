import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mode

plt.style.use('dark_background')

df = pd.read_csv("csv_operacion6.csv")

def ClassificationFunc(ID):   

    Edad = df['Edad']
    
    if Edad <= 20:
        return "10_20"
    elif Edad <= 30 and Edad > 20:
        return "21_30"
    elif  Edad > 31:
        return "31_60"

df = df.reset_index()
df['Peso'] = df['ID'].transform(ClassificationFunc)

def scatterClassification(df, x_column, y_column, label_column):
    colors = ["green", "gray", "yellow"]
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[i])
    
    ax.set_title("Index de edades en las olimpiadas")
    ax.set_xlabel("Año")
    ax.set_ylabel("Edad") 
    ax.legend()
    plt.savefig("Edades en las Olimpiadas.png")
    plt.close()

def euclidean_value(p_1, p_2) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))

def k_nearest_neightbors(points, labels, input_data, k):
    input_value = [
        [euclidean_value(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_value
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

scatterClassification(df, "Año", "Edad", "ID")

df = pd.DataFrame()
df['x'] = df['Año']
df['y'] = df['Edad']
df['label'] = df['ID']

list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]

points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(
    points,
    labels,
    [np.array([5, 100]), np.array([8, 200]), np.array([10, 300]), np.array([12, 400])],
    5,
)

print(kn)

#No se pudo profe jaja:(