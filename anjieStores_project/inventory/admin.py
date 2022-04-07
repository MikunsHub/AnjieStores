from django.contrib import admin

# Register your models here.

from .models import Employee,Products,Orders,ProductType,Suppliers,Cashier,Transactions

admin.site.register([Employee,Products,Orders,ProductType,Suppliers,Cashier,Transactions])