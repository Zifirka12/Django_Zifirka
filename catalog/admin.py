from django.contrib import admin
<<<<<<< HEAD
from catalog.models import Product, Category


@admin.register(Product)
class ZidirAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
=======

# Register your models here.
>>>>>>> f5a89dbfa3b67e95ccc87a50d5bd8b6040a43f0b
