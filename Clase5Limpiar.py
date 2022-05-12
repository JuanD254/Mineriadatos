# Imports
import pandas as pd
import re
from typing import Tuple
from datetime import datetime
from tabulate import tabulate

def categorize(name:str)->str:
    if 'PREPARATORIA' in name or 'PREPA' in name:
        return 'PREPARATORIA'
    if 'FACULTAD' in name or 'FAC' in name:
        return 'FACULTAD'
    if 'HOSPITAL' in name:
        return 'HOSPITAL'
    if 'CENTRO' in name or 'CTRO.' in name or 'C' in name or 'INVESTIGAC' in name:
        return 'CENTRO'
    if 'SECRETARÍA' in name or 'SECRETARIA' in name or 'SRIA.' in name or 'DIRECCIÓN' in name or 'DIRECCION' in name or \
        'DEPARTAMENTO' in name or 'DEPTO.' in name or 'CONTROLARIA' in name or 'AUDITORIA' in name or 'TESORERIA' in name \
        or 'ESCOLAR' in name or 'ABOGACIA' in name or 'JUNTA' in name or 'RECTORIA' in name or 'IMAGEN' in name:
        return 'ADMIN'
    return 'OTRO'

def remove_repeated_number(str_repeated_value:str)->float:
    if (type(str_repeated_value)!=str):
        str_repeated_value = str(str_repeated_value)
    str_sin_0 = re.sub("^0+", '', str_repeated_value)
    str_sin_coma = str_sin_0.replace(',', '')
    num = 0.0
    mitad = int(len(str_sin_coma)/2)
    if len(str_sin_coma) % 2 == 0:
        num = float(str_sin_coma[0:mitad])
    return num

def extract_int_number(str_value:str)->int:
    str_value_clean = re.findall(r'[\d,\.]*', str_value)[0]
    str_sin_0 = re.sub("^0+", '', str_value_clean)
    str_sin_coma = str_sin_0.replace(',', '')
    return float(str_sin_coma)

def remove_repeated_date(str_date_repeated:str)->datetime:
    return datetime.strptime(str_date_repeated[0:8], '%Y%m%d')

def limpiar_area(area:str)->Tuple[float, float]:
    str_en_partes = re.findall(r'[\d,\.]*', area)
    str_en_partes.remove('2')
    blancos = str_en_partes.count('')
    for blanco in range(0, blancos):
        str_en_partes.remove('')
    km_str = str_en_partes[0]
    km_float = remove_repeated_number(km_str)
    mi_str = str_en_partes[1]
    mi_float = float(mi_str.replace(',',''))
    return (km_float, mi_float)

#Función nueva que cree para eliminar cadenas con corchetes
def eliminar_corchete(str_value:str):
    str_value_corchete=str(str_value + '[a]')
    cad_cor=re.sub(r'\[([A-Za-z0-9_]+)\]','', str_value_corchete)
    return cad_cor

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("csv/estados.csv")
df = df.drop(['Coat of arms'], axis=1)
# print(df.columns)
df.columns = ['estado',
        'nombre_oficial', 
        'capital', 'ciudad_mas_grande', 'area', 'poblacion_2020',
        'num_de_municipios', 'lugar',
        'fecha_de_admision']
# print(df.columns)
df['lugar'] = df['lugar'].transform(remove_repeated_number)
df['poblacion_2020'] = df['poblacion_2020'].transform(remove_repeated_number)
df['fecha_de_admision'] = df['fecha_de_admision'].transform(remove_repeated_date)
df['num_de_municipios'] = df['num_de_municipios'].transform(extract_int_number)
areas = df['area'].transform(limpiar_area).to_list()
df['estado'] = df['estado'].transform(eliminar_corchete)
df['area_km2'] = [a[0] for a in areas]
df['area_mi'] = [a[1] for a in areas]
df = df.drop(['area'], axis=1)
print_tabulate(df)
#df.to_csv("csv/estados_nuevo.csv", index=False)