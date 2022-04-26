from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Employee,Products,ProductType,Sales
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from .inventory_utils import *
import json, sys

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

def add_products(request):
    productsType = ProductType.objects.filter(status = 1)
    context = {
        "productsType": productsType
    }
    return render(request,'inventory/add_products.html',context)

def add_products_ajax(request):
    response_data = {'status':'failed','msg':''}
    
    try:
        print("Getting form data...")
        prod_name = request.POST.get('prod_name')
        manufacturer = request.POST.get('manufacturer')
        catID = int(float(request.POST.get('prodID')))
        qty = int(float(request.POST.get('qty')))
        exp_date = parse_date(request.POST.get('exp_date'))
        price = int(float(request.POST.get('price')))
        barcode = int(float(request.POST.get('barcode')))

        new_product = Products(
            productsID = 4,
            productName=prod_name,
            manufacturer=manufacturer,
            Barcode=barcode,
            Price=price,
            ExpiryDate=exp_date,
            quantity=qty,
            productTypeID=ProductType.objects.filter(productTypeID = catID).first(),
            status = 1
        ).save()
        print("Added to database")
    except:
        response_data['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

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
    products = Products.objects.filter(status = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.productsID, 'name':product.productName, 'price':float(product.Price)})
    
    context = {
        "products": products,
        'product_json' : json.dumps(product_json)
    }
    return render(request, 'inventory/pos.html',context)

def save_basket(request):
    response_data = {'status':'failed','msg':''}

    myTableArray = json.loads(request.POST.get('myTableArray'))
    
    try:
        total = get_total(myTableArray)
        sales = Sales(sub_total=total, grand_total = total, noOfItems=len(myTableArray)).save()
        print(total)
        print(myTableArray)
    except:
        response_data['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(response_data), content_type="application/json")


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


def test2(request):
    products = Products.objects.filter(status = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.productsID, 'name':product.productName, 'price':float(product.Price)})
    # print("prod_json",product_json)
    context = {
        
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    
    return render(request,'inventory/test2.html',context)



def test_save(request):
    response_data = {}
    resp = {'status':'failed','msg':''}
    
    if request.POST.get('action') == 'post':
        print("hiiii")
        productID = request.POST.get('productID')
        productName = request.POST.get('productName')
        qty = request.POST.get('qty')
        total = request.POST.get('total')
        myTableArray = request.POST.get('randData')
        arr = json.loads(request.POST.get('arr'))
        # nums = json.loads(myTableArray)
        # print(nums)

        response_data['productID'] = productID
        response_data['productName'] = productName
        response_data['qty'] = qty
        response_data['total'] = total
        response_data['myTableArray'] = myTableArray
        response_data['arr'] = arr

        print(response_data)

    return HttpResponse(json.dumps(response_data), content_type="application/json")
    
def test_save2(request):
    
    response_data = {}

    myTableArray = request.POST.get('myTableArray')
    arr = json.loads(request.POST.get('arr'))
    print(arr)

    print(myTableArray)

    # print(response_data)

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')

