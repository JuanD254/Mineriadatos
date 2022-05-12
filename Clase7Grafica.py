# Clase 7: Grafica

import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

