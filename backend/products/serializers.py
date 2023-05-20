from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Product, Category, Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tagname']

class CategorySerializer(ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['id', 'name']
       


class ProductSerializer(ModelSerializer):
    tags = TagSerializer(many=True, required = False)
    category = CategorySerializer(required = False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'category',
            'tags',
        ]

class CreateProductSerializer(ModelSerializer):
    tags = TagSerializer(many=True, required = False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'category',
            'tags',
        ]

    def create(self, validated_data):

        tags_data = None
        if 'tags' in validated_data.keys():
          tags_data = validated_data.pop('tags')
        product = Product.objects.create(**validated_data)
        
        if tags_data is not None :
            for tag_data in tags_data:
                tag = Tag.objects.get_or_create(**tag_data)
                product.tags.add(tag[0])

        product.save()
        return product




