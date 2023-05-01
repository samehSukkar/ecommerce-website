
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminUserOrReadOnly
from products.serializers import ProductSerialzer , CategorySerialzer
from products.models import Product, Category


class ProductListCreateView(ListCreateAPIView):
    model = Product
    serializer_class = ProductSerialzer
    permission_classes = [IsAdminUserOrReadOnly]
   
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


class CategoryListCreateView(ListCreateAPIView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerialzer
    permission_classes = [IsAdminUserOrReadOnly]

