# ***Гугл таблицы в csv файл***
> **Преобразует гугл таблицу по ссылке и сохраняет в csv файл**
## Установка | install
```
pip install recipientgsheets
```
## Пример
### Импорт и инициализация

```python
from recipientgsheets import RecipientGoogleSheets

tableid = '1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0'
encoding = 'utf-8'
save_directory = 'table.csv'

gttc = RecipientGoogleSheets(tableid, encoding, save_directory)  # Инициализация класса
```
### Методы
```python
tocsv() # Делает из Гугл таблицы csv файл

get_column(column_num) # Возвращает колонку таблицы по её номеру

get_line(line_num) # Возвращает строку таблицы по её номеру

get_cell(column_num,line_num) # Возвращает нужную ячейку в str
```

## Где найти tableid ?
>Найти ID таблицы можно на том месте , где находится **рука**                                     
>https://docs.google.com/spreadsheets/d/:wave:/edit#gid=0

## Примечание
>Важно чтобы таблица была открытой для общего доступа!

## Полезные ссылки
>[Страница на PyPi](https://pypi.org/project/recipientgsheets)



