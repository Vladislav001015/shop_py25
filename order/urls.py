from rest_framework.routers import DefaultRouter
from django.urls import path, include
from order.views import OrderModeViewSet

router = DefaultRouter()
router.register('', OrderModeViewSet)

urlpatterns = [
    path('', include(router.urls))
]