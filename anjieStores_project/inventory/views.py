from django.shortcuts import render
from .models import Test, Employee
# def index(request):
#     return HttpResponse("Hello, welcome to Anjie Stores")

kpi = "50,000"

def index(request):
    # context = {
    #     "order":kpi,
    #     "Total_Sales":"190,000",
    #     "Profit": "30,000"
    # }
    # a_Test= Test.objects.all()
    employee = Employee.objects.get(stateOfOrigin="Ekiti")
    print(employee)
    context = {
        # "a_Test": a_Test,
        "staff_no":"1234",
        "full_name":"Ayomikun Ogunjuyigbe",
        "employee": employee
    }
    return render(request, 'inventory/index.html',context)

# def user_mgt(request):
#     pass
