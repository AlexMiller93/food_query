from django.db.models import Count
from rest_framework import generics
from foods.models import Food, FoodCategory
from foods.serializers import FoodCategorySerializer

# Create your views here.

"""
В выборку попадают только Блюда у которых `is_publish=True`.
Если в категории нет блюд (или все блюда данной категории
имеют `is_publish=False`) - не включаем ее в выборку.
"""

""" 
Раздел меню 1
    Блюдо 1
        ...
    Блюдо 2
    ...
    Блюдо n

"""


class FoodsAPIListView(generics.ListAPIView):
    """ Список разделов меню, в которых есть хотя бы одно блюдо и у которых `is_publish=True`"""
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        """ Переопределение метода get_queryset """
        
        # выборка блюд, у которых `is_publish=True` 
        # в виде списка словарей с ключами категория и количество 
        # с сортировкой по умолчанию
        
        active_foods = Food.objects \
            .filter(is_publish=True) \
            .values('category') \
            .annotate(count=Count('category')) \
            .order_by()
            
        # список первичных ключей по ключу 'категория' с разделами меню из запроса active_foods
        allowed_ids = [item['category'] for item in active_foods]
        
        # вывод разделов меню с ключами из списка
        categories = FoodCategory.objects.filter(id__in=allowed_ids)
        return categories