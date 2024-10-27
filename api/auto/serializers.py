from rest_framework import serializers
from .models import Auto, Category, Image
from django.core.files import File
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")

class ImageFieldFromURL(serializers.ImageField):
    def to_internal_value(self, data):
# Проверяем, если data - это URL
        if data.startswith("http") or data.startswith("https"):
# Открываем URL и читаем его содержимое
            response = urlopen(data)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(response.read())
            img_temp.flush()
# Создаем объект File из временного файла
            img = File(img_temp)
            return img
        return super().to_internal_value(data)

class ImageSerializer(serializers.ModelSerializer):
    img = ImageFieldFromURL()

    class Meta:
        model = Image
        fields = ("id", "name", "img")

class AutoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True) # Указана связь с категориями
    img = ImageFieldFromURL()

    class Meta:
        model = Auto
        fields = ['id', 'title', 'content', 'time_create', 'time_update', 'public', 'categories', 'img','img1','img2','img3','img4', 'price', 'owners', 'gearbox','mileage','engine','power','year']

    def create(self, validated_data):
        return Auto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.public = validated_data.get('public', instance.public)
        instance.img = validated_data.get('img', instance.img)
        instance.img1 = validated_data.get('img1', instance.img1)
        instance.img2 = validated_data.get('img2', instance.img2)
        instance.img3 = validated_data.get('img3', instance.img3)
        instance.img4 = validated_data.get('img4', instance.img4)
        instance.price = validated_data.get('price', instance.price)
        instance.owners = validated_data.get('owners', instance.owners)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.engine = validated_data.get('engine', instance.engine)
        instance.power = validated_data.get('power', instance.power)
        instance.year = validated_data.get('year', instance.year)
        instance.gearbox = validated_data.get('year', instance.gearbox)
        instance.save()
        return instance