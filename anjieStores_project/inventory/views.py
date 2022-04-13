from django.shortcuts import render,redirect
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
    itemCount = ItemCount.objects.all()
    myFilterPOS = ProductPOSFilter(request.GET, queryset=products)
    products = myFilterPOS.qs
    # print(products)
    cart= {}
    totalAmtCart = {}
    # print(cart)
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        qty = request.POST.get("productqty")
        # print("qty =",qty)
        
        for product in products:
            # print(product.Price)
            price = product.Price
            cart["price"] = price
            cart["productName"] = product.productName
            cart["qty"] = int(qty)
            total = get_info(cart)
            save_cart(cart)
            totalAmtCart["total"] = total
            print("total=",total)
        # return redirect("pos")
        # if form.is_valid():
        #     pass  # does nothing, just trigger the validation
    else:
        form = ItemForm()

    print(cart)
    context = {
        "products": products,
        "myFilterPOS": myFilterPOS,
        "form": form,
        "cart": cart,
        "totalAmtCart":totalAmtCart
    }
    return render(request, 'inventory/pos.html',context)

def checkout(request):
    cart = get_cart()
    context = {
        "cart":cart
    }
    return render(request, 'inventory/checkout.html',context)

def usr_mgt(request):
    return render(request, 'inventory/user_mgt.html')