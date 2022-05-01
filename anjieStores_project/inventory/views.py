from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Employee,Products,ProductType,Sales
from .forms import ProductsForm,EmployeeForm
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from .inventory_utils import *
import json, sys
from users.views import *

@login_required(login_url='login_page')
def index(request):
    employee = Employee.objects.all()
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

from django.db.models import Sum

@login_required(login_url='login_page')
def dashboard(request):
    sales = Sales.objects.all()
    total_sales = sales.count()
    tot_returns = Sales.objects.all()
    tot_returns = int(sum(tot_returns.values_list('grand_total', flat=True)))
    top_sales = Sales.objects.all().order_by('-grand_total')[:5]
    print(top_sales)
    context = {
        "returns": tot_returns,
        "total_sales": total_sales,
        "top_sales": top_sales
    }
    return render(request, 'inventory/dashboard.html',context)

def products(request):
    products = Products.objects.all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {
        "products": products,
        "myFilter": myFilter
    }
    return render(request, 'inventory/products.html',context)

@login_required(login_url='login_page')
def add_products(request):

    form = ProductsForm()
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    context = {
        "form": form
    }
    return render(request,'inventory/add_products.html',context)

@login_required(login_url='login_page')
def edit_products(request,pk):

    product = Products.objects.get(productsID=pk)
    form = ProductsForm(instance=product)
    if request.method == "POST":
        form = ProductsForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    context = {
        "form": form
    }
    return render(request,'inventory/add_products.html',context)


@login_required(login_url='login_page')
def categories(request):
    productsType = ProductType.objects.all()

    prodTypefilter = ProductTypeFilter(request.GET, queryset=productsType)
    context = {
        "productsType": productsType,
        "prodTypefilter": prodTypefilter
    }
    return render(request, 'inventory/categories.html',context)

@login_required(login_url='login_page')
def order(request):
    return render(request, 'inventory/order.html')

@login_required(login_url='login_page')
def pos(request):
    products = Products.objects.filter(status = 1)
    product_json = []
    for product in products:
        product_json.append({'id':product.productsID, 'name':product.productName,'quantity':product.quantity, 'price':float(product.Price)})
    
    context = {
        "products": products,
        'product_json' : json.dumps(product_json)
    }
    return render(request, 'inventory/pos.html',context)

@login_required(login_url='login_page')
def save_basket(request):
    response_data = {'status':'failed','msg':''}

    myTableArray = json.loads(request.POST.get('myTableArray'))

    #TODO :: put safety net for empty basket transactions
    
    try:
        total = get_total(myTableArray)
        sales = Sales(sub_total=total, grand_total = total, noOfItems=len(myTableArray)).save()
        val = update_stock(myTableArray)
        # print(total)
        print(myTableArray)
    except:
        response_data['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required(login_url='login_page')
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


@login_required(login_url='login_page')
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


@login_required(login_url='login_page')
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

@login_required(login_url='login_page') 
def test_save2(request):
    
    response_data = {}

    myTableArray = request.POST.get('myTableArray')
    arr = json.loads(request.POST.get('arr'))
    print(arr)

    print(myTableArray)

    # print(response_data)

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required(login_url='login_page')
def usr_mgt(request):
    employees = Employee.objects.all()

    context= {
        "employees": employees
    }
    return render(request, 'inventory/user_mgt.html',context)

@login_required(login_url='login_page')
def employee_profile(request):
    form = EmployeeForm(initial={'user': request.user})

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("usr_mgt")

    context = {
        "form":form
    }
    return render(request, 'inventory/employee.html',context)



# def add_products_ajax(request):
#     response_data = {'status':'failed','msg':''}
    
#     try:
#         print("Getting form data...")
#         prod_name = request.POST.get('prod_name')
#         manufacturer = request.POST.get('manufacturer')
#         catID = int(float(request.POST.get('prodID')))
#         qty = int(float(request.POST.get('qty')))
#         exp_date = parse_date(request.POST.get('exp_date'))
#         price = int(float(request.POST.get('price')))
#         barcode = int(float(request.POST.get('barcode')))

#         new_product = Products(
#             productsID = 4,
#             productName=prod_name,
#             manufacturer=manufacturer,
#             Barcode=barcode,
#             Price=price,
#             ExpiryDate=exp_date,
#             quantity=qty,
#             productTypeID=ProductType.objects.filter(productTypeID = catID).first(),
#             status = 1
#         ).save()
#         print("Added to database")
#     except:
#         response_data['msg'] = "An error occured"
#         print("Unexpected error:", sys.exc_info()[0])
#     return HttpResponse(json.dumps(response_data), content_type="application/json")