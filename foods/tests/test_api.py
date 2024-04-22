from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from foods.serializers import (
    FoodCategorySerializer, 
    FoodListSerializer, FoodSerializer, 
    PublishedFoodListSerializer, 
    PublishedFoodSerializer)
from foods.models import Food, FoodCategory

class FoodApiListTestCase(APITestCase):
    def test_get_published_foods(self):
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
        
        
        url = reverse('foods')
        
        response = self.client.get(url)
        # serializer_data = FoodCategorySerializer(food_1).data
        serializer_data = FoodCategorySerializer([food_1, food_2], many=True).data
        print(serializer_data)
        print('\n')
        print(response.data)
        # self.assertEqual(serializer_data, response.data)