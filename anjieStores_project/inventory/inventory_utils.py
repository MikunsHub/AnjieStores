# from .models import Employee,Products,ProductType


# def productTypeFilter(request):
#     productsType = ProductType.objects.filter(productsType=)


def get_info(cart):
    price = cart.get('price')
    qty = cart.get('qty')
    totalAmount = price * qty
    return totalAmount