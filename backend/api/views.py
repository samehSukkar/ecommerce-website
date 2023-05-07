
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .permissions import IsAdminUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductSerialzer , CategorySerialzer, TagSerialzer
from products.models import Product, Category, Tag
from orders.models import CartItem, Order, OrderItem
from orders.serializers import CartItemSerialzer, CreateCartItemSerialzer, OrderSerialzer, UserSerializer
from rest_framework.views import APIView, Response
from rest_framework.exceptions import status
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser

class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerialzer
    permission_classes = [IsAdminUserOrReadOnly]
    parser_classes = (MultiPartParser, JSONParser)

    def get_queryset(self):
    
        queryset = Product.objects.order_by('-pk')

        category = self.request.query_params.get('category')

        if category is not None  and isinstance(category, int) :
           queryset =  queryset.filter(category = category)
         
        tag = self.request.query_params.get('tag')
        if tag is not None :
            queryset =  queryset.filter(tag__id = tag)

        return queryset
   
class PorductRUDAPIView(RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    permission_classes = [IsAdminUserOrReadOnly]



class CategoryListCreateView(ListCreateAPIView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerialzer
    permission_classes = [IsAdminUserOrReadOnly]


class TagListCreateView(ListCreateAPIView):
    model = Tag
    queryset = Tag.objects.all().order_by('tagname')
    serializer_class = TagSerialzer
    permission_classes = [IsAdminUserOrReadOnly]
    


class CartItemListCreateView(ListCreateAPIView):
    model = CartItem
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
    
    def get_serializer_class(self, *args, **kwargs):
        if (self.request.method == 'POST'):
            return CreateCartItemSerialzer 
        else:
            return CartItemSerialzer
         
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)


class orderListView(ListAPIView):
    model = Order
    serializer_class = OrderSerialzer
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

        serialized_order = OrderSerialzer(order)
        return Response(serialized_order.data, status=status.HTTP_201_CREATED)
    


class UserRegesterationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

