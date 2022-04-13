# from .models import Employee,Products,ProductType
import json

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
    return json.load(open(r"C:\Users\HP PC\Documents\PersonalProjects\AnjieStores\anjieStores_project\inventory\temp_storage\cart.json"))

