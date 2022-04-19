from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Employee,Products,ProductType
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter

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
    myFilterPOS = ProductPOSFilter(request.GET, queryset=products)
    products = myFilterPOS.qs
    
    context = {
        "products": products,
        "myFilterPOS": myFilterPOS,
    }
    return render(request, 'inventory/pos.html',context)



def cart_add(request):
    cart = 0
    if request.method == "POST":
        cart = request.POST.get("addtocart")
        # print(cart)
        print(request.headers.get('Hx-Request'))
    if request.headers.get('Hx-Request') == "true" :
        print(cart)
        # return only the result to be replaced
        return HttpResponse(str(cart))
    else:
        return render(request,'inventory/partial.html',{'cart':cart})
    


def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')




