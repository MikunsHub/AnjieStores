from django.shortcuts import render
from .models import Employee,Products,ProductType
from .filters import ProductFilter,ProductTypeFilter


def index(request):
    
    employee = Employee.objects.get(stateOfOrigin="Ekiti")
    productsType = ProductType.objects.all()
    products = Products.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    prodTypefilter = ProductTypeFilter(request.GET, queryset=productsType)
    products = myFilter.qs
    productsType = prodTypefilter.qs
    context = {
        "staff_no":"1234",
        "full_name":"Ayomikun Ogunjuyigbe",
        "employee": employee,
        "productsType": productsType,
        "products": products,
        "myFilter": myFilter,
        "prodTypefilter": prodTypefilter
    }
    return render(request, 'inventory/index.html',context)

def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def products(request):
    return render(request, 'inventory/products.html')

def categories(request):
    return render(request, 'inventory/categories.html')

def order(request):
    return render(request, 'inventory/order.html')

def pos(request):
    return render(request, 'inventory/pos.html')

def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')