import pandas as pd
import statsmodels.api as sm
import numbers
import matplotlib.pyplot as plt
from tabulate import tabulate
from typing import Tuple

# Predicciones (Forecasting)

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def regresion_lineal(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    bands = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]
    print_tabulate(pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0])
    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    r_2_t = pd.read_html(model.summary().tables[0].as_html(),header=None,index_col=None)[0]
    return {'m': coef.values[1], 'b': coef.values[0], 'r2': r_2_t.values[0][3], 'r2_adj': r_2_t.values[1][3], 'low_band': bands['[0.025'][0], 'hi_band': bands['0.975]'][0]}

def plt_lr(df: pd.DataFrame, x:str, y: str, m: float, b: float, r2: float, r2_adj: float, low_band: float, hi_band: float, colors: Tuple[str,str]):
    fixed_x = transform_variable(df, x)
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[ m * x + b for _, x in fixed_x.items()], color=colors[0])
    plt.fill_between(df[x],
                     [ m * x  + low_band for _, x in fixed_x.items()],
                     [ m * x + hi_band for _, x in fixed_x.items()], alpha=0.2, color=colors[1])
            
df = pd.read_csv("csv/netflix_catalogo_drama.csv")
df_by_rat = df.groupby(["rating"])[["release_year"]].agg('mean')
df_by_rat.reset_index(inplace=True)
#print(df_by_rat)
a = regresion_lineal(df_by_rat, "rating", "release_year")
plt_lr(df=df_by_rat, x="rating", y="release_year", colors=('red', 'green'), **a)

plt.xticks(rotation=90)
plt.savefig('img/reglineal_anio_prom_rating_prediccion.png')
plt.close()