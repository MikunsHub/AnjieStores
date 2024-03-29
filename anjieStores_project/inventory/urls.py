from django.urls import path

from . import views

urlpatterns = [
    # path('boy/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('order/', views.order, name='order'),
    path('pos/', views.pos, name='pos'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('usr_mgt/', views.usr_mgt, name='usr_mgt'),
]

