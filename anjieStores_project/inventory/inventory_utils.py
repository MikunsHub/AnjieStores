# from .models import Employee,Products,ProductType
import json
from django.shortcuts import HttpResponse
# def productTypeFilter(request):
#     productsType = ProductType.objects.filter(productsType=)


def get_info(cart):
    price = cart.get('price')
    qty = cart.get('qty')
    totalAmount = price * qty
    return totalAmount

def save_cart(cart):
    with open(r"C:\Users\HP PC\Documents\PersonalProjects\AnjieStores\anjieStores_project\inventory\temp_storage\cart.json", "w") as outfile:
        json.dump(cart, outfile,indent = 4)

def get_cart():
    with open(r"C:\Users\HP PC\Documents\PersonalProjects\AnjieStores\anjieStores_project\inventory\temp_storage\cart.json") as d:
        dictData = json.load(d)
        print(dictData)
        print(type(dictData))
    return dictData

def write_json(new_data, filename=r"C:\Users\HP PC\Documents\PersonalProjects\AnjieStores\anjieStores_project\inventory\temp_storage\cart.json"):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.update(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def get_total(arr):
    lenght = len(arr)

    total = 0
    for i in range(lenght):
        for key in arr[i]:
            if key == "total":
                total += arr[i]["total"]
    return total

