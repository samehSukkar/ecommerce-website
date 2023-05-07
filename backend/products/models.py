from django.db import models
from django.core.validators import MinValueValidator



class Product(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/' , default='/default/default.png')
    description = models.TextField(max_length = 200, blank=True)
    price = models.FloatField(null = False , validators=[MinValueValidator(0)]) 
    category = models.ForeignKey('Category', models.SET_NULL ,null=True)
    tags =  models.ManyToManyField('Tag' , blank=True, null=True, default=None)

    def __str__ (self):
        return self.name

class Tag(models.Model):
    tagname =  models.CharField(max_length=30)
    
    def __str__ (self):
        return self.tagname



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__ (self):
        return self.name
    
