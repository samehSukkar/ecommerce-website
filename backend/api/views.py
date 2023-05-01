from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUserOrReadOnly
from products.serializers import ProductSerialzer
from products.models import Product
from rest_framework import authentication 
from .pagination import PageNumberCountPagination


class ProductListCreateView(ListCreateAPIView):
    model = Product
    queryset = Product.objects.all().order_by('-pk')
    serializer_class = ProductSerialzer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [ authentication.TokenAuthentication,
                               authentication.SessionAuthentication ]
    pagination_class = PageNumberCountPagination
   
class PorductRUDAPIView(RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [ authentication.TokenAuthentication,
                               authentication.SessionAuthentication ]





