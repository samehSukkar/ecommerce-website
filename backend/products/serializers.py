from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Product, Category, Tag


class TagSerialzer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductSerialzer(ModelSerializer):
    # tags = TagSerialzer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerialzer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



