from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        total = 0
        items = OrderItem.objects.filter(order=self.id)
        for item in items :
            total += item.product.price *item.quantity
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    order = models.ForeignKey(Order, on_delete= models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
    
