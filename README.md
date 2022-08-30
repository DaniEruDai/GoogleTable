# ***Получение данных с Google таблиц***
____
### Установка
```
pip install recipientgsheets
```
### Импорт и инициализация
```python
from recipientgsheets import RecipientGoogleSheets

tableid = '1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0'
encoding = 'utf-8'
save_directory = 'table.csv'

gttc = RecipientGoogleSheets(tableid,encoding,save_directory) # Инициализация класса
```
### Где найти tableid ?
>Найти ID таблицы можно на том месте , где находится **ExampleID**                                     
>https://docs.google.com/spreadsheets/d/ExampleID/edit#gid=0
### Методы
```python
tocsv() # Делает из Гугл таблицы csv файл

get_column(column_num) # Возвращает колонку таблицы по её номеру

get_line(line_num) # Возвращает строку таблицы по её номеру

get_cell(column_num,line_num) # Возвращает нужную ячейку в str
```
## Примечание
>Важно чтобы таблица была открытой для общего доступа!
## Полезные ссылки
>[Страница на GitHub](https://github.com/DaniEruDai/recipientgsheets)
> | [Страница на PyPi](https://pypi.org/project/recipientgsheets)


