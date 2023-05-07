from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Product, Category, Tag


class TagSerialzer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tagname']

class CategorySerialzer(ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['id', 'name']
       


class ProductSerialzer(ModelSerializer):
    tags = TagSerialzer(many=True, required = False)
    category = CategorySerialzer(required = False)

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

        category_data = validated_data.pop('category')
        product = Product.objects.create(**validated_data)
        
        cat = Category.objects.get_or_create(**category_data)[0]
        product.category = cat

       
        if tags_data is not None :
            for tag_data in tags_data:
                tag = Tag.objects.get_or_create(**tag_data)
                product.tags.add(tag[0])

        product.save()
        return product




