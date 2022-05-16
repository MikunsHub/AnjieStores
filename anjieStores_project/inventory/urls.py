from django.urls import path

from . import views

urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('products/add_products/', views.add_products, name='add_products'),
    path('products/edit_products/<str:pk>', views.edit_products, name='edit_products'),
    path('products/delete_products/<str:pk>', views.delete_products, name='delete_products'),
    path('categories/', views.categories, name='categories'),
    path('categories/add_categories/', views.add_categories, name='add_categories'),
    path('order/', views.order, name='order'),
    path('pos/', views.pos, name='pos'),
    path('save_basket/', views.save_basket, name='save_basket'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('test_save/', views.test_save, name='test_save'),
    path('test_save2/', views.test_save2, name='test_save2'),
    path('usr_mgt/', views.usr_mgt, name='usr_mgt'),
    path('edit_profile/', views.employee_profile, name='employee_profile'),
    path('test_task/', views.test_task, name='test_task'),
    path('check_stock_task/', views.check_stock_task, name='check_stock_task'),
]
