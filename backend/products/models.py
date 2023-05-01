from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model) :

    name = models.CharField(max_length=30)
    description = models.TextField(max_length = 200, blank=True)
    price = models.FloatField(null = False , validators=[MinValueValidator(0)]) 
    
