from django.urls import path

from foods.views import FoodsAPIListViewSet

# router = routers.SimpleRouter()
# router.register(r'foods', AllPublishedFoodsViewSet, basename='foods')
# router.register(r'foods', FoodsAPIListViewSet, basename='foods')

# 127.0.0.1/api/v1/foods/

urlpatterns = [
    path(
        'api/v1/foods', 
        view=FoodsAPIListViewSet.as_view(), 
        name='foods')
]
