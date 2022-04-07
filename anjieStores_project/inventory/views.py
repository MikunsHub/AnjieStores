from django.shortcuts import render
from .models import Employee,Products,ProductType
# def index(request):
#     return HttpResponse("Hello, welcome to Anjie Stores")



def index(request):
    # context = {
    #     "order":kpi,
    #     "Total_Sales":"190,000",
    #     "Profit": "30,000"
    # }
    employee = Employee.objects.get(stateOfOrigin="Ekiti")
    productsType = ProductType.objects.all()
    products = Products.objects.all()
    # for product in products:
    #     print(product.productName)
    #     print(product.Price)
    print(productsType)
    context = {
        "staff_no":"1234",
        "full_name":"Ayomikun Ogunjuyigbe",
        "employee": employee,
        "productsType": productsType,
        "products": products
    }
    return render(request, 'inventory/index.html',context)

# def user_mgt(request):
#     pass
