from rest_framework import serializers
from .models import CartItem, OrderItem, Order
from products.models import Product
from django.contrib.auth.models import User 
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth import password_validation

class ItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image']


class CartItemSerializer(serializers.ModelSerializer):
    product = ItemProductSerializer() 
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CreateCartItemSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = CartItem
            fields = ['product', 'quantity'] 
    

class OrderItemSerializer(serializers.ModelSerializer):
     product = ItemProductSerializer()
     class Meta:
            model = OrderItem
            fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)
    total = serializers.ReadOnlyField()
    class Meta:
         model = Order
         fields = ['id' , 'user', 'date', 'orderitem_set' , 'total']

    


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta :
            model = User
            fields = ['username', 'email','password', 'password2']

    def validate_password(self, password):
       
        user = User(
                username=self.initial_data['username'],
                email = self.initial_data['email']
                )
        password_validation.validate_password(password, user=user)

        return password

    def validate_password2(self, password2):
         
        if  password2 != self.initial_data['password'] : 
            raise ValidationError(
                'The two password fields did not match.',
                code="password_mismatch",
            )
        
        return password2
    

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],  
        )

        user.set_password(validated_data['password'])
        user.save()
        return user