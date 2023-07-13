from django.contrib import admin
from .models import Category, Product, Image, Manufacturer, ManufacturerManager, Company, Client, Manager, Order, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Manufacturer)
admin.site.register(ManufacturerManager)
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Order)
admin.site.register(Review)
