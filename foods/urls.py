from django.urls import path

from foods.views import FoodsAPIListView

# 127.0.0.1/api/v1/foods/

urlpatterns = [
    path(
        'api/v1/foods/',
        view=FoodsAPIListView.as_view(),
        name='foods')
]
