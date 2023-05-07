from django.contrib import admin
from .models import Product, Category, Tag
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ["name", "description", "price"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   list_display = ["tagname"]
   fields = ['tagname']

