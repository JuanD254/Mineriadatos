import pandas as pd
import matplotlib.pyplot as plt

def analysis_drama(file_name:str)->None:
    df = pd.read_csv(file_name)
    df_by_yc = df.groupby(['rating', 'type'])['release_year'].count()
    #print(df_by_yc)
    df_by_yc.plot(y = 'release_year', legend=False, figsize=(32,20))
    plt.savefig("img/plot_drama_year.png")
    plt.close()

def analysis_year(file_name:str)->None:
    df = pd.read_csv(file_name)
    df_by_year_rating = df.groupby(['release_year', 'type'])['rating'].count()
    #print(df_by_year_rating)
    df_by_year_rating.plot(y = 'rating', legend=False, figsize=(40,25))
    plt.savefig("img/plot_netflix_year.png")
    plt.close()
    
analysis_drama("csv/netflix_catalogo_drama.csv")
analysis_year("csv/netflix_catalogo_anio.csv")