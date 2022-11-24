"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():

    with open('clusters_report.txt') as c_report:
        rows = c_report.readlines()

    #Filtramos las filas con datos (No tomar el header)

    rows = rows[4:]

    # datos del cluster [int,int, float, string]
    cluster_list = []
    cluster = [0, 0, 0, '']

    for row in rows:
        if re.match('^ +[0-9]+ +', row):
            indx, amount, percent, *sentence = row.split()

            cluster[0] = int(indx)
            cluster[1] = int(amount)
            cluster[2] = float(percent.replace(',','.'))

            sentence.pop(0)
            sentence = ' '.join(sentence)
            cluster[3] += sentence

        elif re.match('^ +[a-z]', row):
            sentence = row.split()
            sentence = ' '.join(sentence)
            cluster[3] += ' ' + sentence

        elif re.match('^\n', row) or re.match('^ +$', row):
            cluster[3] = cluster[3].replace('.', '') 
            cluster_list.append(cluster)
            cluster = [0, 0, 0, '']
    
    df = pd.DataFrame (cluster_list, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df
