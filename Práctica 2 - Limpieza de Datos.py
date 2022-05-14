import pandas as pd

#Práctica 2 - Limpieza de datos
def Práctica_2():
    df = pd.read_csv("athlete_events.csv") 
    df = df.drop(['Games'], axis=1)

    df['Medal'] = df['Medal'].replace(to_replace = ["Gold", "Silver", "Bronze"], value = ["Oro", "Plata", "Bronce"])
    df['Season'] = df['Season'].replace(to_replace = ["Summer", "Winter"], value = ["Verano", "Invierno"])
    df.columns = ['ID', 'Nombre', 'Sexo', 'Edad', 'Estatura', 'Peso', 'Equipo', 'Comité', 'Año', 'Temporada', 'Ciudad', 'Deporte', 'Evento', 'Medalla']
    
    df.to_csv('csv_limpio.csv')

Práctica_2()