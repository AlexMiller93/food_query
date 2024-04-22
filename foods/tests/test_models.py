from django.test import TestCase
from foods.models import Food, FoodCategory


class FoodsTest(TestCase):
    """ Test module for Food model """
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = User.objects.create_user(username='auth')
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.cat1 = FoodCategory.objects.create(
            name_ru='Test category 1')
        self.cat2 = FoodCategory.objects.create(
            name_ru='Test category 2', order_id=5)
        
        self.food1=Food.objects.create(
            category= self.cat1, 
            code=100,
            name_ru='Test food 1',
            cost=10.00
            )
        
        self.food2=Food.objects.create(
            category= self.cat2, 
            code=200,
            name_ru='Test food 2',
            cost=20.00,
            is_publish=False
            )
        
    def test_code_label(self):
        food=Food.objects.get(id=1)
        field_label = food._meta.get_field('code').verbose_name
        self.assertEquals(field_label,'Код поставщика')
        
    def test_name_ru_max_length(self):
        food=Food.objects.get(id=1)
        max_length = food._meta.get_field('name_ru').max_length
        self.assertEquals(max_length,255)
        
    def test_cost_max_digits(self):
        food=Food.objects.get(id=1)
        max_digits = food._meta.get_field('cost').max_digits
        self.assertEquals(max_digits,10)
        
    def test_str_representation(self):
        food=Food.objects.get(id=1)
        expected_object_name = f'{food.name_ru}'
        self.assertEquals(expected_object_name,'Test food 1')
        
    def test_food_label(self):
        '''Проверка заполнения verbose_name'''
        
        field_verboses = {
                'category': 'Раздел меню',
                'is_vegan': 'Вегетарианское меню',
                'code': 'Код поставщика',
                'cost': 'Цена',
                'is_publish': 'Опубликовано',
                'additional': 'Дополнительные товары'
            }
        
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.food1._meta.get_field(field).verbose_name,
                    expected_value, error_name)
                
class FoodCategoryTest(TestCase):
    """ Test module for FoodCategory model """
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.cat1=FoodCategory.objects.create(
            name_ru='Test category 1')
        self.cat2=FoodCategory.objects.create(
            name_ru='Test category 2', order_id=5)
    
    def test_name_en_label(self):
        cat=FoodCategory.objects.get(id=1)
        field_label = cat._meta.get_field('name_en').verbose_name
        self.assertEquals(field_label,'Название на английском')
        
    def test_name_ch_max_length(self):
        cat=FoodCategory.objects.get(id=1)
        max_length = cat._meta.get_field('name_ch').max_length
        self.assertEquals(max_length,255)
        
    def test_str_representation(self):
        cat=FoodCategory.objects.get(id=1)
        expected_object_name = f'{cat.name_ru}'
        self.assertEquals(expected_object_name,'Test category 1')
        
    def test_food_category_label(self):
        '''Проверка заполнения verbose_name'''
        
        field_verboses = {
                'name_ru': 'Название на русском',
                'name_en': 'Название на английском',
                'name_ch': 'Название на китайском'
            }
        
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                error_name = f'Поле {field} ожидало значение {expected_value}'
                self.assertEqual(
                    self.cat1._meta.get_field(field).verbose_name,
                    expected_value, error_name)