# Приложение QRKot

## Суть проекта:

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии проекта:

- Python 3.7.9
- Fastapi 0.78.0
- SQLAlchemy 1.4.36
- Alembic
- uvicorn 0.17.6
- aiohttp 0.8.0

## Запуск проекта:

- Клонируем репозиторий: **git clone [Приложение QRKot](https://github.com/Olga-Zholudeva/cat_charity_fund)**
- Cоздаем и активировируем виртуальное окружение: **python3 -m venv env source env/bin/activate**
- Устанавливаем зависимости из файла requirements.txt: **pip install -r requirements.txt**
- Запускаем проект: **uvicorn app.main:app --reload**
- Для просмотра документации загрузите файл openapi.json на сайт https://redocly.github.io/redoc/
- Запросы к API можно отправлять, например, через Postman либо со страницы **http://localhost:8000/docs**

## Действия пользователей:

- Проекты содаются, редактируются и удаляются только администраторами
- Любой пользователь может посмотреть все проекты
- Зарегистрированный пользователь может создать пожертвование, которое автоматически будет распределно по открытым проектам. Зарегистрированному пользователю доступен список всех его пожертвований.

<details open>

  **<summary>Более детальная информация по проекту</summary>**

    Любой посетитель сайта (в том числе неавторизованный) может посмотреть список всех проектов.
    Суперпользователь может: 
    - создавать проекты,
    - удалять проекты, в которые не было внесено средств,
    - изменять название и описание существующего проекта, устанавливать для него новую требуемую сумму (но не меньше уже внесённой).
    Никто не может менять через API размер внесённых средств, удалять или модифицировать закрытые проекты, изменять даты создания и закрытия проектов.
    Любой зарегистрированный пользователь может сделать пожертвование.
    Зарегистрированный пользователь может просматривать только свои пожертвования.
    Информация о том, инвестировано пожертвование в какой-то проект или нет, обычному пользователю недоступна.
    Суперпользователь может просматривать список всех пожертвований, при этом ему выводятся все поля модели.
    Редактировать или удалять пожертвования не может никто.

    Процесс «инвестирования»
    Сразу после создания нового проекта или пожертвования должен запускаться процесс «инвестирования» (увеличение invested_amount как в пожертвованиях, так и в проектах, установка значений fully_invested и close_date, при необходимости). 
    Если создан новый проект, а в базе были «свободные» (не распределённые по проектам) суммы пожертвований — они автоматически  инвестируются в новый проект. То же касается и создания пожертвований: если в момент пожертвования есть открытые проекты, эти пожертвования автоматически зачисляются на их счета.

</details>

## Проект выполнен:

 **Ольга Жолудева**
