from rest_framework import viewsets
from foods.models import Food
from foods.serializers import FoodListSerializer
# Create your views here.

"""
В выборку попадают только Блюда у которых `is_publish=True`.
Если в категории нет блюд (или все блюда данной категории
имеют `is_publish=False`) - не включаем ее в выборку.
"""


class FoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """ """
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer
