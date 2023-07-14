from django.contrib import admin
from .models import Category, Product, Image, Manufacturer, ManufacturerManager, Client, ClientManager, StaffManager, \
    Order, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Manufacturer)
admin.site.register(ManufacturerManager)
admin.site.register(Client)
admin.site.register(ClientManager)
admin.site.register(StaffManager)
admin.site.register(Order)
admin.site.register(Review)
