from functools import reduce
import pandas as pd
import requests

from dataclasses import dataclass


@dataclass
class table(list):
    data: list

    def tindex(self, ellement: int | str | float, exact_str=True) -> dict | list | tuple:
        """
        Получение индекса из таблицы
        P.S - Если таблица представленна в виде колонок , то результаты принимают вид (строка,колонка)
        """

        """
        В coincidences записывается список всех 
        строк похожих на изначальную (ellement).
        В случае с "точной строкой" будет всего
        1 эллемент  
        """
        coincidences = set(
            reduce(
                lambda x1, x2: x1 + x2, [[s for s in i if ellement.lower() in s.lower()] for i in self.data]))
        if exact_str:
            coincidences = {ellement}

        elif len(coincidences) > 1 and exact_str:
            return ()

        dict_result = {}
        for ellement in coincidences:
            rows = [found_object for found_object in self.data if ellement in found_object]
            result = []
            for row in rows:
                index_column = row.index(ellement)
                index_row = self.data.index(row)
                result.append((index_column, index_row))

            if exact_str:
                if len(result) == 1:
                    result = result[0]
                return result

            elif not exact_str:
                if len(result) == 1:
                    result = result[0]
                dict_result[ellement] = result

        return dict_result

    def to_list(self) -> list:
        return list(self.data)

    def to_tuple(self) -> tuple:
        return tuple(self.data)

    def cell(self, column_num: int, row_num: int):
        return self.data[row_num][column_num]


class GoogleTable:
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

    def rows(self, row_num: int = None) -> table:
        rows = self.__df.values.tolist()
        if row_num is None:
            return table(rows)
        elif isinstance(row_num, int):
            return table(rows[row_num])

    def columns(self, column_num: int = None, column_names_as_first_ellement: bool = False) -> table:
        all_table_rows = self.__df.values.tolist()
        all_columns = []
        for num in range(len(max(all_table_rows))):
            column = [str(i[num]) for i in all_table_rows]

            """!Добавляет название столбца первым эллементом списка!"""
            if column_names_as_first_ellement:
                column.insert(0, self.__df.columns[num])

            all_columns.append(column)

        if column_num is None:
            return table(all_columns)
        elif isinstance(column_num, int):
            return table(all_columns[column_num])

    def cell(self, column_num: int, row_num: int) -> str or int or float:
        return self.columns(column_num).data[row_num]

    def column_names(self) -> list:
        return self.__df.columns

    def tofile(self, filename: str = 'file', file_format: str = 'xlsx'):
        url = f'https://docs.google.com/spreadsheets/d/{self.__tableid}/export?format={file_format}&id={self.__tableid}'
        r = requests.get(url)
        with open(f'{filename}.{file_format}', 'wb') as f:
            f.write(r.content)
