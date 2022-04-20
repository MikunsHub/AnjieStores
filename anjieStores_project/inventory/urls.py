from django.urls import path

from . import views

urlpatterns = [
    # path('boy/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('categories/', views.categories, name='categories'),
    path('order/', views.order, name='order'),
    path('pos/', views.pos, name='pos'),
    path('test/', views.test, name='test'),
    path('test_save/', views.test_save, name='test_save'),
    path('usr_mgt/', views.usr_mgt, name='usr_mgt'),
]
