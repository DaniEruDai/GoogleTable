# ***Получение данных с Google таблиц***
____
### Установка
```cmd
pip install googletable
```
### Импорт и инициализация

```python
from GoogleTable import GoogleTable

tableid = '1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0'
gid = '0'
encoding = 'utf-8'

GoogleTable(tableid,gid,encoding)
```
### Где найти tableid ?
>tableid - ID таблицы гугл (Под верхними стрелками)
> 
>gid - ID листа таблицы (Над нижними стрелками )

                                           ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    https://docs.google.com/spreadsheets/d/1iVSut_5LLcXAeecJI73y0EmltL8mwg-9hEHaWP2UOp0/edit#gid=0  
                                                                                        ↑↑↑↑↑↑↑↑↑↑


### Примечание
> ## Важно чтобы таблица была открыта для общего доступа!
### Полезные ссылки
>[Страница на GitHub](https://github.com/DaniEruDai/GoogleTable)
> | [Страница на PyPi](https://pypi.org/project/googletable/)
