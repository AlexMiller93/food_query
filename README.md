# API для ресторана

## Установка

Склонировать репозиторий на локальную машину

```
git clone https://github.com/AlexMiller93/food_query.git
```

## Создание виртуального окружения

```
python -m venv venv
```

Активация виртуального окружения

```
venv\Scripts\activate
```

Для корректной работы проекта необходимо установить все необходимые пакеты и зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

Нужно создать копию файла .env для хранения секретных данных согласно приведенному примеру .env.example

## Создание учетной записи админа

```
python manage.py createsuperuser
```

## Запуск сервера

```
python manage.py runserver
```

## Задание

Даны модели FoodCategory и Food для ресторана, даны сериализаторы FoodSerializer и FoodListSerializer.

Стек: Django\DRF

Написать запрос, куда попадают только блюда у которых `is_publish=True`. Если в категории нет блюд (или все блюда данной категории имеют `is_publish=False`) - не включаем ее в выборку.

Написать View который вернет для API 127.0.0.1/api/v1/foods/
JSON следующего формата:

```
    [
        {
            "id":1,
            ...
            <!-- поля  FoodListSerializer -->
            "foods":[
            {
                "internal_code":100,
                ...
                <!--  поля  FoodSerializer -->
                "additional":[
                    200
                ]
            },
            ]
        },
    ]
```

## Выполнение задания

1. В файле views.py добавлен class FoodsAPIListView для выборки категорий блюд, в которых есть блюда с условием `is_publish=True`

2. В файле serializers.py добавлены сериализаторы PublishedFoodListSerializer, PublishedFoodSerializer, FoodCategorySerializer для вывода блюд с фильтрацией по признаку `is_publish=True`

3. Добавлены тесты для проверки корректной работы api
Тесты находятся в папке foods/tests

4. После запуска сервера и перейдя по ссылке 127.0.0.1/api/v1/foods/ можно увидеть выборку категорий блюд в заданном формате JSON

5. Была проведен рефакторинг кода, добавлены функции и методы для удобной работы и поддержкой api

Для запуска тестов необходимо запустить одну из следующих команд:

```
python manage.py test foods.tests.test_serializers
python manage.py test foods.tests.test_api
python manage.py test foods.tests.test_models
python manage.py test foods.tests.test_views
```
