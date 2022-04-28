# from .models import Employee,Products,ProductType
import json
from django.shortcuts import HttpResponse
from .models import Products
import sys
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
    length = len(arr)

    total = 0
    for i in range(length):
        for key in arr[i]:
            if key == "total":
                total += arr[i]["total"]
    return total

def update_stock(arr):
    """
    This function takes the immediate products bought and updates the
    stock in the supermarket warehouse.
    """
    length = len(arr)

    for i in range(length):
        for key in arr[i]:
            if key == "qty":
                try:
                    print(arr[i]["name"])
                    sale_qty = arr[i]["qty"]
                    product = Products.objects.get(productsID=arr[i]["id"])
                    
                    product.quantity -= int(float(sale_qty))
                    product.save()

                except AttributeError as e:
                    print(e)
                    # response_data['msg'] = "An error occured"
                    print("Unexpected error:", sys.exc_info()[0])
                
    return "working"

