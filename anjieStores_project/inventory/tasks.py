from celery import shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from .models import Products

logger = get_task_logger(__name__)

@shared_task
def check_stock_cron():
    """
    Saves latest image from Flickr
    """
    product = Products.objects.filter(status=1)
    # print(f"{product.productName} has a quantity of",product.quantity)
    for i in product:
        # print(i.quantity)
        if i.quantity <= i.min_quantity:
            print(f"{i.productName} has low stock")
            i.quantity += i.order_quantity
            i.save()
            print("stock updated")
        else:
            print("There are enough products in the store")

@shared_task(bind=True)
def test_func(self):

    for i in range(10):
        print(i)

    return "Done"

@shared_task(bind=True)
def check_stock(self):
    product = Products.objects.filter(status=1)
    # print(f"{product.productName} has a quantity of",product.quantity)
    for i in product:
        # print(i.quantity)
        if i.quantity >= i.min_quantity:
            print(f"{i.productName} has a quantity of",i.quantity)
            print("stock status very good")
        else:
            print("low stock")
            i.quantity += i.order_quantity
            i.save()
    return "Done"