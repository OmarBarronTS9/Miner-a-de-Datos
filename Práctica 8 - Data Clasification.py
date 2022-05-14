import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from typing import Tuple, Dict, List
import numpy as np
from functools import reduce
from scipy.stats import mode

plt.style.use('dark_background')

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))


def normalize_distribution(dist: np.array, n: int) -> np.array:
    b = dist - min(dist) + 0.000001
    c = (b / np.sum(b)) * n
    return np.round(c)


def create_distribution(mean: float, size: int) -> pd.Series:
    return normalize_distribution(np.random.standard_normal(size), mean * size)

def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

def scatter_group_by(file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str):
    plt.figure(figsize=(8,5))
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.title("Ganadores de Medallas")
    plt.savefig(file_path)
    plt.show()

groups = [(20, 20, "grupo1"), (80, 40, "grupo2"), (200, 200, "grupo3")]
df = pd.read_csv("csv_operacion/csv_operacion7.csv")
scatter_group_by("img/Data Classification.png", df, "Año", "Sexo", "Medalla")
list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in df.itertuples(index=False, name=None)
]
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]