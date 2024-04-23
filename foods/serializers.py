from rest_framework import serializers
from foods.models import Food, FoodCategory


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='internal_code')

    class Meta:
        model = Food
        fields = (
            'internal_code', 'code', 'name_ru', 'description_ru',
            'description_en', 'description_ch', 'is_vegan',
            'is_special', 'cost', 'additional')


class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')


class PublishedFoodListSerializer(serializers.ListSerializer):
    """ Сериализатор списка блюд, фильтрует данные,
        оставляя только блюда с is_publish == True"""

    child = FoodSerializer()

    def to_representation(self, data):
        data = data.filter(is_publish=True)
        return super().to_representation(data)


class PublishedFoodSerializer(FoodSerializer):
    """
        Сериализатор расширяет  функциональность FoodSerializer,
        указывая  PublishedFoodListSerializer
        как сериализатор множества объектов 
    """

    class Meta(FoodSerializer.Meta):
        list_serializer_class = PublishedFoodListSerializer


class FoodCategorySerializer(FoodListSerializer):
    """ Сериализатор расширяет функциональность FoodListSerializer,
    используя  PublishedFoodSerializer для вывода блюд,
    что обеспечивает фильтрацию по признаку is_publish == True """

    foods = PublishedFoodSerializer(source='food', many=True, read_only=True)
