# Clase 6: Análisis
# Funciones de agregación:
# min, max, moda, conteo, sumatoria, 
# Funcion generadora de momentos = media, varianza, desviación estándar, asimetria, kurtosis
# Álgebra relacional:
# transposición, selección, proyección, uniones, joins, agrupación

import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def analysis(file_name:str)->pd.DataFrame:
    df = pd.read_csv(file_name)
    df["hab_x_km2"] = df["poblacion_2020"] / df["area_km2"]
    df["hab_x_mi"] = df["poblacion_2020"] / df["area_mi"]
    #print(sum(df["poblacion_2020"]))
    return df

df = analysis("csv/estados_nuevo.csv")
print_tabulate(df.head())
print_tabulate(df.describe())
print(df['poblacion_2020'].sum())