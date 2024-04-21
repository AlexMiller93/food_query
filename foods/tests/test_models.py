from django.test import TestCase
from foods.models import Food, FoodCategory


class FoodsTest(TestCase):
    """ Test module for Foods model """
    
    @classmethod
    def setUpTestData(cls):
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
        
    # def test_first_name_label(self):
    #     author=Author.objects.get(id=1)
    #     field_label = author._meta.get_field('first_name').verbose_name
    #     self.assertEquals(field_label,'first name')
        
    # def test_first_name_max_length(self):
    #     author=Author.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEquals(max_length,100)
    
    def test_str_representation(self):
        food=Food.objects.get(id=1)
        expected_object_name = f'{food.name_ru}'
        self.assertEquals(expected_object_name,'Test food 1')