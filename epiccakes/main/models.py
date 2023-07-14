from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    biscuit = 'bis'
    sandy = 'san'
    puff = 'puf'
    waffle = 'waf'
    air = 'air'
    tiny = 'tin'
    custards = 'cus'

    TYPE = [
        (biscuit, 'Бисквитные'),
        (sandy, 'Песочные'),
        (puff, 'Слоеные'),
        (waffle, 'Вафельные'),
        (air, 'Воздушные'),
        (tiny, 'Крошковые'),
        (custards, 'Заварные')
    ]

    title = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=3, choices=TYPE)
    category = models.ManyToManyField(Category, related_name='products')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='products')
    weight = models.IntegerField(null=True, blank=True)
    best_before_date = models.IntegerField(null=True, blank=True)
    storage_temperature = models.IntegerField(null=True, blank=True)
    proteins = models.IntegerField(null=True, blank=True)
    fats = models.IntegerField(null=True, blank=True)
    carbohydrates = models.IntegerField(null=True, blank=True)
    energy_value = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255, blank=True)
    data = models.URLField()

    def __str__(self):
        return self.product


class Manufacturer(models.Model):
    active = 'act'
    inactive = 'ina'

    STATUS = [
        (active, 'Действующий'),
        (inactive, 'Недействующий')
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    office = models.CharField(max_length=255, blank=True)
    metro_station = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    status = models.CharField(max_length=3, choices=STATUS)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ManufacturerManager(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='managers')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'


class Client(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    office = models.CharField(max_length=255, blank=True)
    metro_station = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ClientManager(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    company = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='managers', blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'


class StaffManager(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    job_title = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}. {self.second_name[0]}.'


class Order(models.Model):
    delivery = 'deli'
    pickup = 'pick'

    DELIV = {
        (delivery, 'Доставка'),
        (pickup, 'Самовывоз')
    }

    cash = 'cash'
    card = 'card'

    PAY = [
        (cash, 'Наличными'),
        (card, 'Банковской картой')
    ]

    processing = 'proc'
    done = 'done'

    STATUS = [
        (processing, 'В работе'),
        (done, 'Выполнено')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    manager = models.ForeignKey(StaffManager, on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField()
    delivery_method = models.CharField(max_length=4, choices=DELIV)
    payment_method = models.CharField(max_length=4, choices=PAY)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=4, choices=STATUS)


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reviews')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    text = models.TextField()
    date_in = models.DateTimeField()
