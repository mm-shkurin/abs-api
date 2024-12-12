from django.contrib import admin
from .models import Category, Image, Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "mileage")
    fields = ("title", "content", "categories", "images", "price", "owners", "mileage", "gearbox", "engine", "power", "year", "user")  # Заменено img на images
    search_fields = ("title",)
    ordering = ("title",)
    filter_horizontal = ["categories", "images"]  # Добавлено images в filter_horizontal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name",)