import pandas as pd
import requests


class GT:
    """
        tableid - ID таблицы гугл (Смотреть на стрелки 'вниз')
        gid - ID листа таблицы (Смотреть на стрелки 'вверх', P.S Первый лист всегда равен нулю)

                                               ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        https://docs.google.com/spreadsheets/d/1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0/edit#gid=0
                                                                                            ↑↑↑↑↑↑↑↑↑↑
    """

    def __init__(self, tableid: str, gid: str = '0', encoding: str = 'utf-8'):
        self.__tableid = tableid
        self.__URL = f'https://docs.google.com/spreadsheets/d/{self.__tableid}' \
                     f'/export?format=csv&id={self.__tableid}&gid={gid} '
        self.__df = pd.read_csv(self.__URL, keep_default_na=False, na_filter=False, encoding=encoding)

    def rows(self, row_num: int = None) -> list:
        rows = self.__df.values.tolist()
        if row_num is None:
            return rows
        elif isinstance(row_num, int):
            return rows[row_num]

    def columns(self, column_num: int = None, column_names_as_first_ellement: bool = False) -> list:
        all_table_rows = self.__df.values.tolist()
        all_columns = []
        for num in range(len(max(all_table_rows))):
            column = [str(i[num]) for i in all_table_rows]

            """!Добавляет название столбца первым эллементом списка!"""
            if column_names_as_first_ellement: column.insert(0, self.__df.columns[num])

            all_columns.append(column)

        if column_num is None:
            return all_columns
        elif isinstance(column_num, int):
            return all_columns[column_num]

    def cell(self, column_num: int, row_num: int) -> str or int or float:
        return str(self.columns(column_num)[row_num])

    def column_names(self):
        return self.__df.columns

    def tofile(self, filename: str = 'file', file_format: str = 'xlsx'):
        url = f'https://docs.google.com/spreadsheets/d/{self.__tableid}/export?format={file_format}&id={self.__tableid}'
        r = requests.get(url)
        with open(f'{filename}.{file_format}', 'wb') as f:
            f.write(r.content)
