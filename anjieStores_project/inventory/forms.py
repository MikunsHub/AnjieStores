from django.forms import ModelForm
from django import forms
from .models import Products, Employee


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        exclude = ['productsID','status']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['employeeID']

        widgets = {
            'user': forms.HiddenInput(),
        }

