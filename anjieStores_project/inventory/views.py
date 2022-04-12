from django.shortcuts import render
from .models import Employee,Products,ProductType,ItemCount
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter
from .forms import ItemForm


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
    products = Products.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {
        "products": products,
        "myFilter": myFilter
    }
    return render(request, 'inventory/products.html',context)

def categories(request):
    productsType = ProductType.objects.all()

    prodTypefilter = ProductTypeFilter(request.GET, queryset=productsType)
    context = {
        "productsType": productsType,
        "prodTypefilter": prodTypefilter
    }
    return render(request, 'inventory/categories.html',context)

def order(request):
    return render(request, 'inventory/order.html')

def pos(request):
    products = Products.objects.all()
    itemCount = ItemCount.objects.all()
    myFilterPOS = ProductPOSFilter(request.GET, queryset=products)
    products = myFilterPOS.qs

    if request.method == 'POST':
        form = ItemForm(request.POST)
        print(request.POST.get("productqty"))
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ItemForm()


    context = {
        "products": products,
        "myFilterPOS": myFilterPOS,
        "form": form
    }
    return render(request, 'inventory/pos.html',context)

def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')