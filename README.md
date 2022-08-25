# ***Гугл таблицы в csv файл***
> **Простая функция , которая преобразует гугл таблицу по ссылке и сохраняет в csv файл**
## Установка | install
```
pip install gtabletocsv
```
## Пример
```python
import gtabletocsv

tableid = '1MZx_UtA_R8VEqZhqG860keRfvrCAEVPBeQ7Q9XjGJHQ'
encoding = 'utf-8'
save_directory = 'table.csv'

gtabletocsv.tocsv(tableid,encoding,save_directory)
```

## Где найти tableid ?
>Найти ID таблицы можно на том месте , где находится **рука**                                     
>https://docs.google.com/spreadsheets/d/:wave:/gviz/tq?tqx=out:csv&sheet' 

## Примечание
>Важно чтобы таблица была открытой для общего доступа!

## Полезные ссылки
>[Страница на PyPi](https://pypi.org/project/gtabletocsv/)



