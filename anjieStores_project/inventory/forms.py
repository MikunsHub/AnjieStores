from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Products, Employee, ProductType, Orders


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        exclude = ['productsID','status']

        widgets = {
            'productName': forms.TextInput(attrs={'class':'form-control'}),
            'Barcode': forms.NumberInput(attrs={'class':'form-control'}),
            'ExpiryDate': forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'Price': forms.NumberInput(attrs={'class':'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control'}),
            'productTypeID': forms.Select(attrs={'class':'form-control'}),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = ProductType
        exclude = ['status']

        widgets = {
            'productType': forms.TextInput(attrs={'class':'form-control'}),
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['employeeID']

        widgets = {
            'user': forms.HiddenInput(),
            'fullName': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
            'doB': forms.NumberInput(attrs={'type':'date', 'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'phoneNo': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'stateOfOrigin': forms.TextInput(attrs={'class':'form-control'}),
            'employmentDate': forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'status': forms.TextInput(attrs={'class':'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control'})
            
        }


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        
        widgets = {
            'orderDate': forms.NumberInput(attrs={'type':'date','class':'form-control'}),
            'productTypeID': forms.Select(attrs={'class':'form-control'}),
        }

