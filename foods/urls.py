from django.urls import include, path
from rest_framework import routers

from foods.views import AllPublishedFoodsViewSet, FoodsAPIListViewSet

router = routers.SimpleRouter()
router.register(r'foods', AllPublishedFoodsViewSet, basename='foods')
# router.register(r'foods', FoodsAPIListViewSet, basename='foods')

# 127.0.0.1/api/v1/foods/

urlpatterns = [
    path('api/v1/', include(router.urls))
]
