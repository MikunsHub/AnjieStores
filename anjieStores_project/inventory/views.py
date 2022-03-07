from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, welcome to Anjie Stores")

kpi = "50,000"

def index(request):
    context = {
        "order":kpi,
        "Total_Sales":"70,000",
        "Profit": "30,000"
    }
    return render(request, 'inventory/index.html',context)

