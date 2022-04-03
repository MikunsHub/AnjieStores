from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    
    return render(request, 'users/signup.html')

def login(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')

    #     try:
    #         user = User.objects.get(username=name)
    #     except:

    # context = {}
    return render(request, 'users/login.html')