import random

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient

from foods.models import Food, FoodCategory
from foods.serializers import FoodCategorySerializer, FoodListSerializer, FoodSerializer

# Create your tests here.

# factory = APIClient()
# request = factory.post('/notes/', {'title': 'new idea'}, format='json')

# class FoodTests(APIClientTest):
#     pass


# initialize the APIClient app
client = Client()


class FoodsTest(TestCase):
    """ Test module for GET foods API """
    
    def setUp(self):
        test_cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        test_cat2 = FoodCategory.objects.create(
            name_ru='Test category 2', order_id=5)
        
        test_food_1 = Food.objects.create(
            category=test_cat1, 
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )
        
        test_food_2 = Food.objects.create(
            category=test_cat2, 
            code=200,
            name_ru='Test food 2',
            cost=20.00,
            is_publish=False
            )
    
    def test_get_published_foods(self):
        # get API response
        response = client.get(reverse('foods'))
        
        
        print(f'Response.data: {response.data}')
        
        # get data from db
        # published_foods = Food.objects.filter(is_publish=True)
        categories = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(categories, many=False)
        
        print(f'Serializer.data: {serializer.data}')
        
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)