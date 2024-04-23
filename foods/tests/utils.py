from foods.models import Food, FoodCategory


def create_test_food_data():
    """ Функция для создания данных классов Food, FoodCategory
        для дальнейшего тестирования """

    cat1 = FoodCategory.objects.create(
        name_ru='Test category 1')
    cat2 = FoodCategory.objects.create(
        name_ru='Test category 2')

    food1 = Food.objects.create(
        category=cat1,
        code=100,
        name_ru='Test food 1',
        cost=10.00
        )
    food2 = Food.objects.create(
        category=cat2,
        code=200,
        name_ru='Test food 2',
        cost=20.00,
        is_publish=False
        )
    food3 = Food.objects.create(
        category=cat1,
        code=300,
        name_ru='Test food 3',
        cost=30.00,
        is_publish=False
        )
    food4 = Food.objects.create(
        category=cat1,
        code=400,
        name_ru='Test food 4',
        cost=25.00
    )
    return ([cat1, cat2], [food1, food2, food3, food4])
