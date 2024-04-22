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
    """ Сериализатор для фильтрации блюд, у которых`is_publish=True` """
    
    child = FoodSerializer()

    def to_representation(self, data):
        data = data.filter(is_publish=True)
        return super().to_representation(data)


class PublishedFoodSerializer(FoodSerializer):
    """ Сериализатор наследуется от FoodSerializer, 
    использует  PublishedFoodListSerializer как list_serializer_class  """
    
    additional = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='internal_code')

    class Meta(FoodSerializer.Meta):
        list_serializer_class = PublishedFoodListSerializer
        

class FoodCategorySerializer(FoodListSerializer):
    """ Сериализатор наследуется от FoodListSerializer, 
    использует  PublishedFoodSerializer для вывода блюд, у которых`is_publish=True`"""
    
    foods = PublishedFoodSerializer(source='food', many=True, read_only=True)