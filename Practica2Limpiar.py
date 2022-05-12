# Imports
import pandas as pd
from datetime import datetime
import datetime
from tabulate import tabulate

def llenar_vacio(fechas: pd.DataFrame)->pd.DataFrame:
    j = 0
    for i in fechas['date_added']:
        f = 'March 03, 2022'
        if pd.isna(i):
            fechas['date_added'][j] = str(f)
            #print(fechas['date_added'][j])
        j = j + 1
    return fechas

def cambiar_ff(fechas: pd.DataFrame)->pd.DataFrame:
    j = 0
    for i in fechas['date_added']:
        if i.find("-") !=-1:
            fechas['date_added'][j] = datetime.datetime.strptime(i, '%d-%b-%y')
            fechas['date_added'][j].strftime('%B %d %Y')
        else:
            fechas['date_added'][j] = datetime.datetime.strptime(i, '%B %d, %Y')
            fechas['date_added'][j].strftime('%B %d %Y')
        j = j + 1
    return fechas

def limpiar_pais(paises: pd.DataFrame)->pd.DataFrame:
    j=0
    for i in paises['country']:
        f = 'Other'
        if pd.isna(i):
            paises['country'][j] = f
            #print(paises['country'][j])
        j = j + 1
    #print(paises['country'])
    return paises

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("C:/Users/juand/Documents/Mineria/csv/netflix.csv")
llenar_vacio(df)
cambiar_ff(df)
limpiar_pais(df)

#print_tabulate(df)
#df.to_csv("csv/netflix_actualizado.csv", index=False)