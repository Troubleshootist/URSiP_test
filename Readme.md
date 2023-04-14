## Тестовое задание для URSiP

Используемые зависимости:
- openpyxl==3.1.2

Используемая БД:
- sqlite

Для запуска проекта:
```shell
python3 main.py
```

По умолчанию БД хранится в памяти. Для изменения пути к 
файлу измеиите в ```main.py```:
```python
db_engine = DBEngine(data=parser.data_rows, sqlite_db_path='<your_path>')
```