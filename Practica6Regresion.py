import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import statsmodels.api as sm
import numbers

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

# Regresión Linear

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        print("Nada")
        return pd.Series([i for i in range(0, len(df[x]))])

def regresion_lineal(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    #print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in range(0, len(df[x]))], color='green')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for x in range(0, len(df[x]))], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'img/reglineal_{y}_{x}.png')
    plt.close()

df = pd.read_csv("csv/netflix_catalogo_drama.csv")
df_by_rat = df.groupby(["rating"])[["release_year"]].agg('mean')
df_by_rat.reset_index(inplace=True)
df_by_rat.columns=["rating", "anio_prom"]
#print_tabulate(df_by_rat.head(13))
regresion_lineal(df_by_rat, "rating", "anio_prom")