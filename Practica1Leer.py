# Funciones
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import csv

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_csv_from_url(url: str) -> pd.DataFrame:
    s = requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

# Netflix
df = pd.read_csv("C:/Users/juand/Downloads/archive/netflix_titles.csv")
print_tabulate(df)
df.to_csv("csv/netflix.csv", index=False)