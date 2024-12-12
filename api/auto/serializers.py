from rest_framework import serializers
from .models import Auto, Image, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'img']


class AutoSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)  # Отображение связанных изображений
    categories = serializers.PrimaryKeyRelatedField(
    many=True,
    queryset=Category.objects.all()
)  # Сериализация категорий по их названию
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )  # Для загрузки новых изображений

    class Meta:
        model = Auto
        fields = [
            'id', 'title', 'content', 'time_create', 'time_update', 'public',
            'categories', 'images', 'uploaded_images', 'price', 'owners', 'mileage',
            'engine', 'power', 'year', 'gearbox', 'user'
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        categories = validated_data.pop('categories', [])
        
        # Создание объекта авто
        auto = Auto.objects.create(**validated_data)

        # Привязка категорий
        if categories:
            auto.categories.set(categories)

        # Привязка новых изображений
        for image_file in uploaded_images:
            image_instance = Image.objects.create(img=image_file, name=image_file.name)
            auto.images.add(image_instance)

        return auto

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', None)
        categories = validated_data.pop('categories', None)

        # Обновление категорий
        if categories is not None:
            instance.categories.set(categories)

        # Обновление изображений
        if uploaded_images:
            for image_file in uploaded_images:
                image_instance = Image.objects.create(img=image_file, name=image_file.name)
                instance.images.add(image_instance)

        # Обновление остальных полей
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = True
        user.save()
        return user