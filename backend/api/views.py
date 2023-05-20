
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .permissions import IsAdminUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductSerializer , CategorySerializer, TagSerializer, CreateProductSerializer
from products.models import Product, Category, Tag
from orders.models import CartItem, Order, OrderItem
from orders.serializers import CartItemSerializer, CreateCartItemSerializer, OrderSerializer, UserSerializer
from rest_framework.views import APIView, Response
from rest_framework.exceptions import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser

class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    parser_classes = (MultiPartParser, JSONParser)
    
    def get_queryset(self):
    
        queryset = Product.objects.order_by('-pk')

        category = self.request.query_params.get('category')
        if category is not None  :
           queryset =  Product.objects.filter(category__id = category)
    
        tag = self.request.query_params.get('tag')
        if tag is not None :
            queryset =  Product.objects.filter(tags__id = tag)

        return queryset
    

    def get_serializer_class(self, *args, **kwargs):
        if (self.request.method == 'POST'):
            return CreateProductSerializer 
        else:
            return ProductSerializer
   
class PorductRUDAPIView(RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]



class CategoryListCreateView(ListCreateAPIView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class TagListCreateView(ListCreateAPIView):
    model = Tag
    queryset = Tag.objects.all().order_by('tagname')
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
class TagRUDView(RetrieveUpdateDestroyAPIView):
    model = Tag
    queryset = Tag.objects.all().order_by('tagname')
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CartItemListCreateView(ListCreateAPIView):
    model = CartItem
    permission_classes = [IsAuthenticated]
   

    def create(self, request, *args, **kwargs):
        item = CartItem.objects.filter(product__id = request.data.get('product'))
        if item.exists() :
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            item = item[0]
            item.quantity += serializer.data['quantity']
            item.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

        return super().create(request, *args, **kwargs)
    

    def get_serializer_class(self, *args, **kwargs):
        if (self.request.method == 'POST'):
            return CreateCartItemSerializer 
        else:
            return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class CartItemRUDView(RetrieveUpdateDestroyAPIView):
    model = CartItem
    permission_classes = [IsAuthenticated]
   
    def get_serializer_class(self, *args, **kwargs):
        if (self.request.method == 'PUT'):
            return CreateCartItemSerializer 
        else:
            return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)



class orderListView(ListAPIView):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('date')


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_cart = CartItem.objects.filter(user=request.user)

        if not user_cart  :
            return Response({"message":"cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
        

        order = Order.objects.create(user=request.user)
        for cart_item in user_cart:
            order_item = OrderItem.objects.create(
                product=cart_item.product,
                quantity=cart_item.quantity,
                order=order
            )
            cart_item.delete()

        serialized_order = OrderSerializer(order)
        return Response(serialized_order.data, status=status.HTTP_201_CREATED)
    


class UserRegesterationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

