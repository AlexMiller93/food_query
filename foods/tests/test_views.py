from django.test import TestCase

from foods.tests.utils import create_test_food_data
from foods.views import FoodsAPIListView


class FoodsViewTestCase(TestCase):
    def setUp(self):
        super().setUp()
        categories, foods = create_test_food_data()
        self.categories = categories
        self.foods = foods

    def test_get_queryset(self):
        """ Метод для тестирования метода get_queryset """

        view = FoodsAPIListView()
        qs = view.get_queryset()
        data = list(qs)
        self.assertEquals(1, len(data))
        category = data[0]
        self.assertEquals(self.categories[0].id, category.id)
