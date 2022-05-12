# Imports
import pandas as pd

def analysis():
    df = pd.read_csv("C:/Users/juand/Documents/Mineria/csv/netflix_actualizado.csv")
    ordfecha = df.sort_values('date_added')
    #ordfecha.to_csv("csv/netflix_orden_fecha.csv", index= False)
    ordanio = df.sort_values('release_year')
    #ordanio.to_csv("csv/netflix_catalogo_anio.csv", index= False)
    #genero_drama(df['listed_in'])  
    # Catalogo según el género de Drama
    searchfor = ['Dramas']
    catal_drama = df[df['listed_in'].str.contains('|'.join(searchfor))]
    #catal_drama.to_csv("csv/netflix_catalogo_drama.csv", index= False)

analysis()
