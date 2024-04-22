from django.test import TestCase

from foods.models import Food, FoodCategory
from foods.serializers import (
    FoodCategorySerializer,
    FoodListSerializer, 
    FoodSerializer, 
    PublishedFoodListSerializer,
    PublishedFoodSerializer
    )


class FoodSerializerTestCase(TestCase):
    def test_get_expected_data(self):
        cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        cat2 = FoodCategory.objects.create(
            name_ru='Test category 2')
        
        food_1 = Food.objects.create(
            category=cat1, 
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )
        
        food_2 = Food.objects.create(
            category=cat2, 
            code=200,
            name_ru='Test food 2',
            cost=20.00,
            is_publish=False
            )
        
        serializer_data = FoodSerializer([food_1, food_2], many=True).data
        
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
        cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        cat2 = FoodCategory.objects.create(
            name_ru='Test category 2')
        
        food_1 = Food.objects.create(
            category=cat1, 
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )
        
        food_2 = Food.objects.create(
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
        
    
# class PublishedFoodListSerializerTestCase(TestCase):
#     def test_get_expected_data(self):
#         cat1 = FoodCategory.objects.create(
#             name_ru='Test category 1')
#         cat2 = FoodCategory.objects.create(
#             name_ru='Test category 2')
        
#         serializer_data = PublishedFoodListSerializer([cat1, cat2], many=True).data
        
#         print(f'\nData: {serializer_data}')
        
#         expected_data = [
#             {
#                 'id': cat1.id,
#                 'name_ru': 'Test category 1',
#                 'name_en': None,
#                 'name_ch': None,
#                 'order_id': 10,
#                 'foods': []
#             },
#             {
#                 'id': cat2.id,
#                 'name_ru': 'Test category 2',
#                 'name_en': None,
#                 'name_ch': None,
#                 'order_id': 10,
#                 'foods': []
#             }
            
#         ]
        
        # self.assertEqual(expected_data, serializer_data)


class PublishedFoodSerializerTestCase(TestCase):
    def test_get_expected_data(self):
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
        serializer_data = PublishedFoodSerializer([cat1, cat2], many=True).data
        
        print(f'\nData: {serializer_data}')
        
        # expected_data = [
        #     {
        #         'id': cat1.id,
        #         'name_ru': 'Test category 1',
        #         'name_en': None,
        #         'name_ch': None,
        #         'order_id': 10,
        #         'foods': [
        #             {
        #                 'internal_code': None,
        #                 'code': 100,
        #                 'name_ru': 'Test food 1',
        #                 'description_ru': None,
        #                 'description_en': None,
        #                 'description_ch': None,
        #                 'is_vegan': False,
        #                 'is_special': False,
        #                 'cost': '10.00',
        #                 'additional': []
        #             },
        #         ]
        #     },
            
        #     {
        #         'id': cat2.id,
        #         'name_ru': 'Test category 2',
        #         'name_en': None,
        #         'name_ch': None,
        #         'order_id': 10,
        #         'foods': []
        #     }
            
        # ]
        
        # self.assertEqual(expected_data, serializer_data)
        
class FoodCategorySerializerTestCase(TestCase):
    def test_get_expected_data(self):
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
        serializer_data = FoodCategorySerializer([cat1, cat2], many=True).data
        
        # print(f'\nData: {serializer_data}')
        
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
                'foods': []
            }
            
        ]
        
        self.assertEqual(expected_data, serializer_data)