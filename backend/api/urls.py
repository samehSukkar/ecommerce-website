from django.urls import path
from .views import ProductListCreateView , PorductRUDAPIView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('auth', obtain_auth_token ),
    path('products',ProductListCreateView.as_view(),name='products'),
    path('products/<int:pk>',PorductRUDAPIView.as_view(),name='product'),
]