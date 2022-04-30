from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from inventory.views import employee_profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    page = "register"
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            auth.login(request,user)
            user_get = form.cleaned_data.get("username")
            messages.success(request,"Account was created successfully for " + user_get)
            return redirect("employee_profile") 
        else:
            messages.error(request,"error occurred during registration")
    return render(request, 'users/signup.html',{'form':form})  #faulty function

def login_page(request):

    # if request.user.is_authenticated:
    #     return redirect('index')

    if request.method == 'POST':
        name = request.POST.get('name').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=name)
            messages.info(request,"User logged in")
        except:
            messages.error(request,"User does not exist")
        
        user = auth.authenticate(request, username=name,password=password)

        if user is not None:
            auth.login(request,user)
            print("I am working")
            return redirect("dashboard")
        else:
            messages.info(request,"Username or Password does not exist")
    return render(request, 'users/login.html')


def logoutUser(request):
    auth.logout(request)
    return redirect('login_page')
    
    
    