from rest_framework import generics, viewsets
from foods.models import Food, FoodCategory
from foods.serializers import FoodListSerializer

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

class AllPublishedFoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """ """
    serializer_class = FoodListSerializer

    def get_queryset(self):
        
        # все разделы меню
        cats = FoodCategory.objects.all()
        
        #? разделы меню где есть блюда -> блюда (is_publish=True)
        if FoodCategory.objects.exists():
            pass
        
        # опубликованные блюда 
        public_foods=cats.food.filter(is_publish=True)
        
        
        return public_foods


class FoodsAPIListViewSet(generics.ListAPIView):
    """ """
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return Food.objects.filter(is_publish=True)
