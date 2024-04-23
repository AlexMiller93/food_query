from django.test import TestCase

from foods.tests.utils import create_test_food_data
from foods.models import Food, FoodCategory
from foods.serializers import (
    FoodCategorySerializer,
    FoodListSerializer,
    FoodSerializer,
    PublishedFoodListSerializer,
    PublishedFoodSerializer
    )


class FoodTestCaseBase(TestCase):
    """ Класс для создания объектов для тестирования сериализаторов """
    def setUp(self):
        super().setUp()
        categories, foods = create_test_food_data()
        self.categories = categories
        self.foods = foods


class FoodSerializerTestCase(FoodTestCaseBase):
    def test_serialize(self):
        serializer_data = FoodSerializer(self.foods[:2], many=True).data

        expected_data = [
            {
                'internal_code': None,
                'code': 100,
                'name_ru': 'Test food 1',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '10.00',
                'additional': []
            },
            {
                'internal_code': None,
                'code': 200,
                'name_ru': 'Test food 2',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '20.00',
                'additional': []
            }

        ]

        self.assertEqual(expected_data, serializer_data)


class FoodListSerializerTestCase(TestCase):
    def test_get_categories_without_foods(self):
        """ Метод для тестирования разделов меню без блюд """

        cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        cat2 = FoodCategory.objects.create(
            name_ru='Test category 2')

        serializer_data = FoodListSerializer([cat1, cat2], many=True).data

        expected_data = [
            {
                'id': cat1.id,
                'name_ru': 'Test category 1',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': []
            },
            {
                'id': cat2.id,
                'name_ru': 'Test category 2',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': []
            }
        ]

        self.assertEqual(expected_data, serializer_data)

    def test_get_categories_with_foods(self):
        """ Метод для тестирования разделов меню с блюдами """

        cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        cat2 = FoodCategory.objects.create(
            name_ru='Test category 2')

        Food.objects.create(
            category=cat1,
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )

        Food.objects.create(
            category=cat2,
            code=200,
            name_ru='Test food 2',
            cost=20.00,
            is_publish=False
            )
        serializer_data = FoodListSerializer([cat1, cat2], many=True).data

        expected_data = [
            {
                'id': cat1.id,
                'name_ru': 'Test category 1',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': [
                    {
                        'internal_code': None,
                        'code': 100,
                        'name_ru': 'Test food 1',
                        'description_ru': None,
                        'description_en': None,
                        'description_ch': None,
                        'is_vegan': False,
                        'is_special': False,
                        'cost': '10.00',
                        'additional': []
                    },
                ]
            },
            {
                'id': cat2.id,
                'name_ru': 'Test category 2',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': [
                    {
                        'internal_code': None,
                        'code': 200,
                        'name_ru': 'Test food 2',
                        'description_ru': None,
                        'description_en': None,
                        'description_ch': None,
                        'is_vegan': False,
                        'is_special': False,
                        'cost': '20.00',
                        'additional': []
                    }
                ]
            }
        ]

        self.assertEqual(expected_data, serializer_data)


class PublishedFoodListSerializerTestCase(FoodTestCaseBase):
    def test_serialize(self):
        serializer_data = PublishedFoodListSerializer(Food.objects.all()).data

        expected_data = [
            {
                'internal_code': None,
                'code': 100,
                'name_ru': 'Test food 1',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '10.00',
                'additional': []
            },
            {
                'internal_code': None,
                'code': 400,
                'name_ru': 'Test food 4',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '25.00',
                'additional': []
            }
        ]

        self.assertEqual(expected_data, serializer_data)


class PublishedFoodSerializerTestCase(FoodTestCaseBase):
    def test_serialize_one(self):
        """ Метод для тестирования сериализатора с одним блюдом """

        serializer_data = PublishedFoodSerializer(
            self.foods[0], many=False).data

        expected_data = {
            'internal_code': None,
            'code': 100,
            'name_ru': 'Test food 1',
            'description_ru': None,
            'description_en': None,
            'description_ch': None,
            'is_vegan': False,
            'is_special': False,
            'cost': '10.00',
            'additional': []
        }

        self.assertEqual(expected_data, serializer_data)

    def test_serialize_many(self):
        """ Метод для тестирования сериализатора с несколькими блюдами """

        serializer_data = PublishedFoodSerializer(
            Food.objects.all(), many=True).data

        expected_data = [
            {
                'internal_code': None,
                'code': 100,
                'name_ru': 'Test food 1',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '10.00',
                'additional': []
            },
            {
                'internal_code': None,
                'code': 400,
                'name_ru': 'Test food 4',
                'description_ru': None,
                'description_en': None,
                'description_ch': None,
                'is_vegan': False,
                'is_special': False,
                'cost': '25.00',
                'additional': []
            }
        ]

        self.assertEqual(expected_data, serializer_data)


class FoodCategorySerializerTestCase(FoodTestCaseBase):
    def test_serialize_with_food(self):
        """ Метод для тестирования сериализатора раздела меню с блюдом """

        serializer_data = FoodCategorySerializer(
            self.categories[0], many=False).data

        expected_data = {
            'id': self.categories[0].id,
            'name_ru': 'Test category 1',
            'name_en': None,
            'name_ch': None,
            'order_id': 10,
            'foods': [
                {
                    'internal_code': None,
                    'code': 100,
                    'name_ru': 'Test food 1',
                    'description_ru': None,
                    'description_en': None,
                    'description_ch': None,
                    'is_vegan': False,
                    'is_special': False,
                    'cost': '10.00',
                    'additional': []
                },
                {
                    'internal_code': None,
                    'code': 400,
                    'name_ru': 'Test food 4',
                    'description_ru': None,
                    'description_en': None,
                    'description_ch': None,
                    'is_vegan': False,
                    'is_special': False,
                    'cost': '25.00',
                    'additional': []
                },
            ]
        }
        self.assertEqual(expected_data, serializer_data)

    def test_serialize_without_food(self):
        """ Метод для тестирования сериализатора раздела меню без блюд """

        serializer_data = FoodCategorySerializer(
            self.categories[1], many=False).data
        expected_data = {
            'id': self.categories[1].id,
            'name_ru': 'Test category 2',
            'name_en': None,
            'name_ch': None,
            'order_id': 10,
            'foods': []
        }
        self.assertEqual(expected_data, serializer_data)

    def test_serialize_many_foods(self):
        """ Метод для тестирования сериализатора
        разделов меню с несколькими блюдами, а также без блюд """

        serializer_data = FoodCategorySerializer(
            self.categories, many=True).data

        expected_data = [
            {
                'id': self.categories[0].id,
                'name_ru': 'Test category 1',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': [
                    {
                        'internal_code': None,
                        'code': 100,
                        'name_ru': 'Test food 1',
                        'description_ru': None,
                        'description_en': None,
                        'description_ch': None,
                        'is_vegan': False,
                        'is_special': False,
                        'cost': '10.00',
                        'additional': []
                    },
                    {
                        'internal_code': None,
                        'code': 400,
                        'name_ru': 'Test food 4',
                        'description_ru': None,
                        'description_en': None,
                        'description_ch': None,
                        'is_vegan': False,
                        'is_special': False,
                        'cost': '25.00',
                        'additional': []
                    },
                ]
            },

            {
                'id': self.categories[1].id,
                'name_ru': 'Test category 2',
                'name_en': None,
                'name_ch': None,
                'order_id': 10,
                'foods': []
            }
        ]

        self.assertEqual(expected_data, serializer_data)
