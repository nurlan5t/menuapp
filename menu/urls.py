from django.urls import path
from menu import views

urlpatterns = [
    path('', views.menus_list, name='menus_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('categories/', views.categories_list, name='categories_list'),
    path('products/', views.products_list, name='products_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
