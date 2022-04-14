from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Employee,Products,ProductType,ItemCount
from .filters import ProductFilter,ProductTypeFilter,ProductPOSFilter
from .forms import ItemForm
from .inventory_utils import get_info, save_cart, get_cart


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
    # print(products)
    # create cart--> a json file
    cart= {}
    totalAmtCart = {}
    # print(cart)
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        qty = request.POST.get("productqty")
        
        for product in products:
            cart= {}
            price = product.Price
            cart["price"] = price
            cart["productName"] = product.productName
            cart["qty"] = int(qty)
            total = get_info(cart)
            save_cart(cart)
            totalAmtCart["total"] = total
            # print("total=",total)
        # return redirect("pos")
        # if form.is_valid():
        #     pass  # does nothing, just trigger the validation
    else:
        form = ItemForm()

    context = {
        "products": products,
        "myFilterPOS": myFilterPOS,
        "form": form,
        # "cart": cart,
        "totalAmtCart":totalAmtCart
    }
    return render(request, 'inventory/pos.html',context)

def checkout(request):
    products = Products.objects.all()
    myFilterPOS = ProductPOSFilter(request.GET, queryset=products)
    products = myFilterPOS.qs

    if request.method == 'POST':
        form = ItemForm(request.POST)
        # if form.is_valid():
        #     pass  # does nothing, just trigger the validation
    else:
        form = ItemForm()

    context = {
        "products": products,
        "form": form,
        "myFilterPOS": myFilterPOS
    }
    return render(request, 'inventory/checkout.html',context)

def cart_add(request):
    cart = 0
    if request.method == "POST":
        cart = request.POST.get("addtocart")
        # print(cart)
        print(request.headers.get('Hx-Request'))
    if request.headers.get('Hx-Request') == None :
        print(cart)
        # return only the result to be replaced
        return HttpResponse(str(cart))
    else:
        return render(request,'inventory/partial.html',{'cart':cart})
    

def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')

# def post_list(request):
#     result = 0
#     if request.method == "POST":
#         num1 = request.POST.get('num_1')
#         num2 = request.POST.get('num_2')
#         result = int(num1) + int(num2)

#     if request.headers.get('Hx-Request') == 'true':
#         # return only the result to be replaced
#         return HttpResponse(str(result))
#     else:
#         return render(request, 'blog/post_list.html', {'result': result})