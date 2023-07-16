from rest_framework import routers
from .views import ProductViewset, CategoryViewset, ManufacturerViewset, ClientViewset, OrderViewset, ReviewViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'product', ProductViewset, basename='product')
router.register(r'category', CategoryViewset, basename='category')
router.register(r'manufacturer', ManufacturerViewset, basename='manufacturer')
router.register(r'client', ClientViewset, basename='client')
router.register(r'order', OrderViewset, basename='order')
router.register(r'review', ReviewViewset, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]
