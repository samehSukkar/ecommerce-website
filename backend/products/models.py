from django.db import models
from django.core.validators import MinValueValidator




class Tag(models.Model):
    tagname =  models.CharField(max_length=30)
    
    def __str__ (self):
        return self.tagname



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__ (self):
        return self.name
    
class Product(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/' , default='/default/default.png')
    description = models.TextField(max_length = 1000, blank=True)
    price = models.FloatField(null = False , validators=[MinValueValidator(0)]) 
    category = models.ForeignKey('Category', default= Category.objects.get_or_create(name='other')[0].id ,  on_delete = models.SET_DEFAULT, )
    tags =  models.ManyToManyField('Tag' , blank=True, null=True, default=None)

    def __str__ (self):
        return self.name
