# from .models import Employee,Products,ProductType
import json
from django.shortcuts import HttpResponse
from .models import Products,ProductSalesAT,Sales
import sys
from django.db.models import Sum,Count



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
                    # print(arr[i]["name"])
                    sale_qty = arr[i]["qty"]
                    product = Products.objects.get(productsID=arr[i]["id"])
                    # print(product)
                    product.quantity -= int(float(sale_qty))
                    product.save()

                except AttributeError as e:
                    print(e)
                    # response_data['msg'] = "An error occured"
                    print("Unexpected error at update_stock:", sys.exc_info()[0])
                
    return "working"

def purchasedItems(arr,sales_id):
    length = len(arr)
    
    for i in range(length):
        for key in arr[i]:
            if key == "qty":
                try:
                    prod_id = int(arr[i]["id"])
                    product = Products.objects.get(productsID=prod_id)
                    sales = Sales.objects.get(id=sales_id)
                    qty_bought = arr[i]["qty"]
                    sub_total = int(arr[i]["total"])
                    selling_price = arr[i]["price"]
                    print(sub_total)
                    sales = ProductSalesAT.objects.create(productsID=product,qtybought=int(qty_bought),subTotal=int(sub_total),price=int(selling_price),salesID=sales)
                except ValueError as e:
                    print(e)
                    print("Unexpected error at purchasedItems:", sys.exc_info()[0])

    return "working"


def mst_commn(arr):
    sales_freq_arr = []
    for i in range(len(arr)):
        dict = {}
        for key in arr[i]:
            if key == "productsID":
                var = ProductSalesAT.objects.filter(productsID=arr[i]["productsID"]).aggregate(Sum('subTotal'))  
                get_prodName = Products.objects.get(productsID=arr[i]["productsID"])

                dict["productsID"] = arr[i]["productsID"]
                dict["productName"] = get_prodName.productName
                dict["count"] = arr[i]["count"]
                dict["total"] = var["subTotal__sum"]
                sales_freq_arr.append(dict)
    return sales_freq_arr

