from django.urls import path
from .views import ProductListCreateView, CategoryListCreateView, PorductRUDAPIView, CartItemListCreateView, orderListView,CreateOrderView,UserRegesterationView,TagListCreateView,CartItemRUDView,CategoryRUDView,TagRUDView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('auth', obtain_auth_token ),
    path('products',ProductListCreateView.as_view(),name='products'),
    path('categories',CategoryListCreateView.as_view(),name='categories'),
    path('categories/<int:pk>',CategoryRUDView.as_view(),name='category'),
    path('tags',TagListCreateView.as_view(),name='tags'),
    path('tags/<int:pk>',TagRUDView.as_view(),name='tag'),
    path('products/<int:pk>',PorductRUDAPIView.as_view(),name='product'),
    path('cart',CartItemListCreateView.as_view(), name='cart'),
    path('cart/<int:pk>',CartItemRUDView.as_view(), name='cartItem'),
    path('orders',orderListView.as_view(), name='orders'),
    path('order/create',CreateOrderView.as_view(), name='create'),
    path('register',UserRegesterationView.as_view(), name='register'),
]