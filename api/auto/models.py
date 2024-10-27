from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"
        ordering = ["id"]

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="auto_images")

    class Meta:
        verbose_name = "фотографию"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото {self.img}"

class Auto(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)
    img = models.ImageField(upload_to="auto_images", blank=True)
    img1 = models.ImageField(upload_to="auto_images", blank=True)
    img2 = models.ImageField(upload_to="auto_images", blank=True)
    img3 = models.ImageField(upload_to="auto_images", blank=True)
    img4 = models.ImageField(upload_to="auto_images", blank=True)
    price = models.CharField(max_length=50, default=0)
    owners = models.CharField(max_length=3, default=0)
    mileage = models.CharField(max_length=7, default=0)
    engine = models.CharField(max_length=3,  default=0)
    power = models.CharField(max_length=3,  default=0)
    year = models.CharField(max_length=4, default=0)
    gearbox = models.CharField(max_length=4, default=0)


    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return f"Автомобиль: {self.title} | Категория: {self.categories.all().first()}"
