from django.urls import reverse
from rest_framework.test import APITestCase

from foods.tests.utils import create_test_food_data


class FoodApiListTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        categories, foods = create_test_food_data()
        self.categories = categories
        self.foods = foods

    def test_get_published_foods(self):
        """ Метод для тестирования получения корректной выборки в api """

        url = reverse('foods')

        response = self.client.get(url)

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
            }
        ]
        self.assertEquals(expected_data, response.data)
