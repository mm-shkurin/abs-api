from django.contrib import admin
from .models import Category, Image, Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "mileage")
    fields = ("title", "content", "categories", "img", 'img1','img2','img3','img4',"price", "owners", "mileage",'gearbox','engine','power','year')
    search_fields = ("title",)
    ordering = ("title",)
    filter_horizontal = ["categories"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    fields = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name",)