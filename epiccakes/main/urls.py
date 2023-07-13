from rest_framework import routers
from .views import ProductViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'product', ProductViewset, basename='product')
# router.register(r'clients', MountainsViewset, basename='clients')
# router.register(r'clients', MountainsViewset, basename='clients')

urlpatterns = [
    path('', include(router.urls)),
]
