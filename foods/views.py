from django.db.models import Count
from rest_framework import generics, viewsets
from foods.models import Food, FoodCategory
from foods.serializers import FoodListSerializer, FoodCategorySerializer

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


class FoodsAPIListViewSet(generics.ListAPIView):
    """ """
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        active_foods = Food.objects \
            .filter(is_publish=True) \
            .values('category') \
            .annotate(count=Count('category')) \
            .order_by()
        allowed_ids = [item['category'] for item in active_foods]
        categories = FoodCategory.objects.filter(id__in=allowed_ids)
        return categories