from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Employee,Products,ProductType
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter
from django.http import JsonResponse
from .inventory_utils import *
import json

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


def test(request):
    products = Products.objects.filter(status = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.productsID, 'name':product.productName, 'price':float(product.Price)})
    print("prod_json",product_json)
    context = {
        
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    
    return render(request,'inventory/test.html',context)

def test_save(request):
    response_data = {}
    resp = {'status':'failed','msg':''}
    
    if request.POST.get('action') == 'post':
        print("hiiii")
        productID = request.POST.get('productID')
        productName = request.POST.get('productName')
        qty = request.POST.get('qty')
        total = request.POST.get('total')
        myTableArray = request.POST.get('myTableArray')

        response_data['productID'] = productID
        response_data['productName'] = productName
        response_data['qty'] = qty
        response_data['total'] = total
        response_data['myTableArray'] = myTableArray

        dict = []
        dict.append(response_data)
        print("dict", dict)
        print(response_data)

        write_json(response_data)
        save_cart(response_data)
        # write_json(response_data)

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    

def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')

# a_dictionary = {"d": 4}

# with open("sample_file.json", "r+") as file:
#     data = json.load(file)
#     data.update(a_dictionary)
#     file.seek(0)
#     json.dump(data, file)
