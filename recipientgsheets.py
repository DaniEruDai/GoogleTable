import pandas as pd
import csv


class RecipientGoogleSheets:

    def __init__(self, tableid:str,encode : str = 'utf-8',save_directory : str = 'result.csv'):
            self.encode = encode
            self.tableid = tableid
            self.save_directory = save_directory

            if encode == 'cp1251': self.separator = ";"
            if encode == 'utf-16': self.separator = "\t"
            if encode == 'utf-8': self.separator = ";"

            self.URL = f'https://docs.google.com/spreadsheets/d/{self.tableid}/gviz/tq?tqx=out:csv&sheet'
            self.df = pd.read_csv(self.URL)

    def tocsv(self):

        with open(self.save_directory, 'w', newline='', encoding=self.encode) as file:
            writer = csv.writer(file, delimiter=self.separator)
            writer.writerow(self.df.columns)

        for line in self.df.values:
            result_line = [str(y) for y in line]
            for ellement in result_line:

                if 'nan' in result_line:
                    for _ in range(result_line.count('nan')):
                        x = result_line.index('nan')
                        result_line[x] = ''

                if ellement.endswith('.0'):
                    result_line[result_line.index(ellement)] = ellement[:-2]

            with open(self.save_directory, 'a', newline='', encoding=self.encode) as file:
                writer = csv.writer(file, delimiter=self.separator)
                writer.writerow(result_line)

    def get_column(self,column_num : int = 0) -> list:

        column =  [str(i[column_num]) for i in self.df.values]
        column.insert(0,[i for i in self.df.columns][column_num])

        for ellement in column:

            if ellement.endswith('.0'): column[column.index(ellement)] = ellement[:-2]

            if 'nan' in column:
                for _ in range(column.count('nan')):
                    index = column.index('nan')
                    column[index] = ''

        return column

    def get_line(self,line_num : int = 0) -> list:

        list_line = [[i for i in self.df.columns]]

        for line in self.df.values:
            result_line = [str(y) for y in line]

            for ellement in result_line:
                if 'nan' in result_line:
                    for _ in range(result_line.count('nan')):
                        x = result_line.index('nan')
                        result_line[x] = ''

                if ellement.endswith('.0'):
                    result_line[result_line.index(ellement)] = ellement[:-2]

            list_line.append(result_line)
        return list_line[line_num]

    def get_cell(self,column_num: int , line_num : int) -> str:
        return str(self.get_column(column_num)[line_num])