import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm

# Prueba de Hipótesis: Hacer una suposición de un dataset y comprobar si está es correcta haciendo análisis
# Spahiro Wills (Checar si el dataset es normal)

def analysis_prueba(file_name:str)->None:
    df = pd.read_csv(file_name)
    df_by_type = df.groupby(["type", "release_year"])[["rating"]].count()
    df_by_type.reset_index(inplace=True)
    df_aux = df_by_type.drop(['release_year'], axis=1)
    #print(df_aux)
    modl = ols("rating ~ type", data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    if anova_df["PR(>F)"][0] < 0.005:
        print("Hay diferencias")
        print(anova_df)
    else:
        print("No hay diferencias")
        print(anova_df)
    df_aux.boxplot(by = 'type', figsize=(32,20))
    plt.savefig("img/boxplot_type.png")

analysis_prueba('csv/netflix_catalogo_drama.csv')