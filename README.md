# ***Гугл таблицы в csv файл***
> **Простая функция , которая преобразует гугл таблицу по ссылке и сохраняет в csv файл**
## Установка | install
```
pip install googletabletocsv
```
## Пример
```python
from googletabletocsv import GtableToCsv

tableid = '1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0'
encoding = 'utf-8'
save_directory = 'table.csv'

gttc = GtableToCsv(tableid,encoding,save_directory) # Инициализация класса
```
### Методы
```
get_column(column_num) # Возвращает колонку таблицы по её номеру

get_line() # Возвращает строку таблицы по её номеру

alltocsv() # Делает из Гугл таблицы csv файл
```

## Где найти tableid ?
>Найти ID таблицы можно на том месте , где находится **рука**                                     
>https://docs.google.com/spreadsheets/d/:wave:/gviz/tq?tqx=out:csv&sheet' 

## Примечание
>Важно чтобы таблица была открытой для общего доступа!

## Полезные ссылки
>[Страница на PyPi](https://pypi.org/project/googletabletocsv)



