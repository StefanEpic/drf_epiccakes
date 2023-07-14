from .models import Category, Product, Image, Manufacturer, ManufacturerManager, Client, ClientManager, StaffManager, \
    Order, Review
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'description']


class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'title', 'data']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'type', 'category', 'manufacturer', 'weight', 'best_before_date', 'storage_temperature',
                  'proteins', 'fats', 'carbohydrates', 'energy_value', 'description', 'price', 'images']

    def create(self, validated_data):
        managers_data = validated_data.pop('managers')
        instance = Manufacturer.objects.create(**validated_data)
        instance.save()

        for manager_data in managers_data:
            ManufacturerManager.objects.create(manufacturer=instance, **manager_data)
        return instance

    def update(self, instance, validated_data):
        if 'managers' in validated_data:
            managers_data = validated_data.pop('managers')

            # if "id" is passed - the manager is updated, otherwise it is added
            for manager in managers_data:
                manager_id = manager.get('id', None)
                if manager_id:
                    inv_manager = ManufacturerManager.objects.get(id=manager_id)
                    inv_manager.first_name = manager.get('first_name', inv_manager.first_name)
                    inv_manager.second_name = manager.get('second_name', inv_manager.second_name)
                    inv_manager.last_name = manager.get('last_name', inv_manager.last_name)
                    inv_manager.phone = manager.get('phone', inv_manager.phone)
                    inv_manager.email = manager.get('email', inv_manager.email)
                    inv_manager.save()
                else:
                    # Fields phone and mail should not be empty
                    manager_phone = manager.get('phone', None)
                    manager_email = manager.get('email', None)
                    if manager_phone and manager_email:
                        if ManufacturerManager.objects.filter(phone=manager_phone).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this phone number')
                        elif ManufacturerManager.objects.filter(email=manager_email).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this email')
                        else:
                            ManufacturerManager.objects.create(company=instance, **manager)
                    else:
                        raise serializers.ValidationError('Update error. Fields phone and mail should not be empty')

            # clearing the manager list when passing an empty list
            managers_dict = dict((i.id, i) for i in instance.managers.all())
            if len(managers_data) == 0:
                for manager in managers_dict.values():
                    manager.delete()

        return super(ManufacturerSerializer, self).update(instance, validated_data)


class ManufacturerManagerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ManufacturerManager
        fields = ['id', 'first_name', 'second_name', 'last_name', 'phone', 'email', 'registration_date']
        read_only_fields = ['id', 'registration_date']


class ManufacturerSerializer(serializers.ModelSerializer):
    managers = ManufacturerManagerSerializer(many=True)

    class Meta:
        model = Manufacturer
        fields = ['title', 'description', 'city', 'street', 'house', 'office', 'metro_station', 'website', 'status',
                  'registration_date', 'managers']
        read_only_fields = ['id', 'status', 'registration_date']

    def create(self, validated_data):
        managers_data = validated_data.pop('managers')
        instance = Manufacturer.objects.create(**validated_data)
        instance.save()

        for manager_data in managers_data:
            ManufacturerManager.objects.create(manufacturer=instance, **manager_data)
        return instance

    def update(self, instance, validated_data):
        if 'managers' in validated_data:
            managers_data = validated_data.pop('managers')

            # if "id" is passed - the manager is updated, otherwise it is added
            for manager in managers_data:
                manager_id = manager.get('id', None)
                if manager_id:
                    inv_manager = ManufacturerManager.objects.get(id=manager_id)
                    inv_manager.first_name = manager.get('first_name', inv_manager.first_name)
                    inv_manager.second_name = manager.get('second_name', inv_manager.second_name)
                    inv_manager.last_name = manager.get('last_name', inv_manager.last_name)
                    inv_manager.phone = manager.get('phone', inv_manager.phone)
                    inv_manager.email = manager.get('email', inv_manager.email)
                    inv_manager.save()
                else:
                    # Fields phone and mail should not be empty
                    manager_phone = manager.get('phone', None)
                    manager_email = manager.get('email', None)
                    if manager_phone and manager_email:
                        if ManufacturerManager.objects.filter(phone=manager_phone).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this phone number')
                        elif ManufacturerManager.objects.filter(email=manager_email).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this email')
                        else:
                            ManufacturerManager.objects.create(company=instance, **manager)
                    else:
                        raise serializers.ValidationError('Update error. Fields phone and mail should not be empty')

            # clearing the manager list when passing an empty list
            managers_dict = dict((i.id, i) for i in instance.managers.all())
            if len(managers_data) == 0:
                for manager in managers_dict.values():
                    manager.delete()

        return super(ManufacturerSerializer, self).update(instance, validated_data)


class ClientManagerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ClientManager
        fields = ['id', 'first_name', 'second_name', 'last_name', 'phone', 'email', 'registration_date']
        read_only_fields = ['id', 'registration_date']


class ClientSerializer(serializers.ModelSerializer):
    managers = ClientManagerSerializer(many=True)

    class Meta:
        model = Client
        fields = ['title', 'description', 'city', 'street', 'house', 'office', 'metro_station', 'website',
                  'registration_date', 'managers']
        read_only_fields = ['id', 'registration_date']

    def create(self, validated_data):
        managers_data = validated_data.pop('managers')
        instance = Client.objects.create(**validated_data)
        instance.save()

        for manager_data in managers_data:
            ClientManager.objects.create(company=instance, **manager_data)
        return instance

    def update(self, instance, validated_data):
        if 'managers' in validated_data:
            managers_data = validated_data.pop('managers')

            # if "id" is passed - the manager is updated, otherwise it is added
            for manager in managers_data:
                manager_id = manager.get('id', None)
                if manager_id:
                    inv_manager = ClientManager.objects.get(id=manager_id)
                    inv_manager.first_name = manager.get('first_name', inv_manager.first_name)
                    inv_manager.second_name = manager.get('second_name', inv_manager.second_name)
                    inv_manager.last_name = manager.get('last_name', inv_manager.last_name)
                    inv_manager.phone = manager.get('phone', inv_manager.phone)
                    inv_manager.email = manager.get('email', inv_manager.email)
                    inv_manager.save()
                else:
                    # Fields phone and mail should not be empty
                    manager_phone = manager.get('phone', None)
                    manager_email = manager.get('email', None)
                    if manager_phone and manager_email:
                        if ClientManager.objects.filter(phone=manager_phone).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this phone number')
                        elif ClientManager.objects.filter(email=manager_email).exists():
                            raise serializers.ValidationError(
                                'Update error. There is already a manager with this email')
                        else:
                            ClientManager.objects.create(company=instance, **manager)
                    else:
                        raise serializers.ValidationError('Update error. Fields phone and mail should not be empty')

            # clearing the manager list when passing an empty list
            managers_dict = dict((i.id, i) for i in instance.managers.all())
            if len(managers_data) == 0:
                for manager in managers_dict.values():
                    manager.delete()

        return super(ClientSerializer, self).update(instance, validated_data)


class StaffManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffManager
        fields = ['first_name', 'second_name', 'last_name', 'phone', 'email', 'job_title', 'registration_date']
        read_only_fields = ['id', 'registration_date']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client', 'product', 'manager', 'amount', 'delivery_method', 'payment_method', 'date', 'status']
        read_only_fields = ['id', 'date', 'status']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['client', 'order', 'rating', 'text', 'date_in']
        read_only_fields = ['id', 'date_in']
