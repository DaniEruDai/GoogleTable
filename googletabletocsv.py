import pandas as pd
import csv

'''
Функция сохраняет Google таблицу в csv файле
ID Google таблицы находится на месте между /d/..../edit
'''
def tocsv(tableid:str,encoding:str,save_directory:str) :
    URL = f'https://docs.google.com/spreadsheets/d/{tableid}/gviz/tq?tqx=out:csv&sheet'
    df = pd.read_csv(URL)

    with open(save_directory, 'w', newline='', encoding= encoding) as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(df.columns)

    for rows in df.values:
        result = [str(x) for x in rows]
        #Удаляет все 'nan' из строк
        if 'nan' in result:
            nan_ammount = result.count('nan')
            for _ in range(nan_ammount):
                result.remove('nan')

        with open(save_directory, 'a', newline='', encoding=encoding) as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(result)

