from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters import rest_framework

from .serializers import ProductSerializer, CategorySerializer, ManufacturerSerializer, ClientSerializer, OrderSerializer, ReviewSerializer
from .models import Product, Category, Manufacturer, Client, Order, Review


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'type', 'category', 'manufacturer', 'price']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'head', 'options']


class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'city', 'metro_station', 'status', 'managers__phone', 'managers__email']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'city', 'metro_station', 'managers__phone', 'managers__email']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['client', 'product', 'manager', 'delivery_method', 'payment_method', 'status']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']


class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['client', 'order', 'rating']
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    # def create(self, request, *args, **kwargs):
    #     serializer = MountainSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             'status': 200,
    #             'message': 'The record was successfully added to the database',
    #             'id': serializer.data['id'],
    #         })
    #
    #     if status.HTTP_400_BAD_REQUEST:
    #         return Response({
    #             'status': 400,
    #             'message': 'Bad request',
    #             'id': None,
    #         })
    #
    #     # if status.HTTP_500_INTERNAL_SERVER_ERROR:
    #     #     return Response({
    #     #         'status': 500,
    #     #         'message': 'Error connecting to database',
    #     #         'id': None,
    #     #     })
    #
    # def partial_update(self, request, *args, **kwargs):
    #     mountain = self.get_object()
    #     serializer = self.get_serializer(mountain, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             'state': 1,
    #             'message': 'The record was successfully updated'
    #         })
    #
    #     else:
    #         return Response({
    #             'state': 0,
    #             'message': serializer.errors
    #         })
