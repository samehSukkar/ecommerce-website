from django.contrib import admin
from .models import Order, CartItem

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','date']
    readonly_fields = ('date',)
    


@admin.register(CartItem)
class OrderAdmin(admin.ModelAdmin):
  pass
  