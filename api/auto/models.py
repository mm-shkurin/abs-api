from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ["id"]

    def str(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100, blank=True)  # Название необязательно
    img = models.ImageField(upload_to="auto_images/%Y/%m/%d")  # Организация файлов по дате загрузки
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "фотографию"
        verbose_name_plural = "Фотографии"

    def str(self):
        return self.name or f"Фото #{self.id}"


class Auto(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, related_name="autos", blank=True)
    images = models.ManyToManyField(Image, related_name="autos", blank=True)
    price = models.CharField(max_length=50, default="0")
    owners = models.CharField(max_length=3, default="0")
    mileage = models.CharField(max_length=7, default="0")
    engine = models.CharField(max_length=3, default="0")
    power = models.CharField(max_length=3, default="0")
    year = models.CharField(max_length=4, default="0")
    gearbox = models.CharField(max_length=4, default="0")
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "Автомобили"

    def str(self):
        categories = ", ".join(cat.name for cat in self.categories.all())
        return f"Автомобиль: {self.title} | Категории: {categories if categories else 'Нет категорий'}"