<div align=center>
    
# Парсер документации pep

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</div>

## Описание проекта

Данный парсер умеет:

1. Собирать данные обо всех документах PEP.
2. Считать количество PEP в каждом статусе и общее количество PEP.
3. Сохранять данные в файлы .csv со списком PEP и со сводкой по статусам.

## Технологии

- Python 3.10.11
- Scrapy 2.5.1

## Запуск проекта

1. Cклонировать проект:

```bash
git clone git@github.com:JustLight1/scrapy_parser_docs_pep.git
```

2. Создать виртуальное окружение и активировать:

```bash
python -m venv venv
source venv/Scripts/activate - windows
```

3. Установить библиотеки из файла requirements.txt:

```bash
pip install -r requirements.txt
```

3. Запустить парсер:

```bash
scrapy crawl pep
```

## Автор:

**Форов Александр**

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
