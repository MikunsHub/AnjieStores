from django.db import models
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    employeeID = models.IntegerField()
    fullName = models.CharField(max_length=35,blank=False,null=False) #not null
    age = models.IntegerField()
    doB = models.DateField()
    position =  models.CharField(max_length=20)
    phoneNo = models.CharField(max_length=14)
    address = models.CharField(max_length=50)
    stateOfOrigin= models.CharField(max_length=10)
    employmentDate = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.fullName


class ProductType(models.Model):
    productTypeID = models.IntegerField()
    productType = models.CharField(max_length=20)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.productType


class Products(models.Model):
    productsID = models.IntegerField(primary_key=True) 
    productName = models.CharField(max_length=30)
    Barcode = models.IntegerField()
    ExpiryDate = models.DateField()
    Price = models.IntegerField()
    manufacturer =  models.CharField(max_length=35)
    quantity = models.IntegerField()
    productTypeID = models.ForeignKey(ProductType,on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.productName

class Suppliers(models.Model):
    suppliersID = models.IntegerField()
    suppliersName = models.CharField(max_length=25)
    suppliersAddress = models.CharField(max_length=25)
    suppliersContact =models.CharField(max_length=11)

    def __str__(self):
        return self.suppliersName


class Orders(models.Model):
    ordersID = models.IntegerField()
    orderDate = models.DateField()
    qtyOrdered = models.IntegerField()
    productsID = models.ForeignKey(Products,on_delete=models.CASCADE)
    employeeID = models.ForeignKey(Employee,on_delete=models.CASCADE)  
    suppliersID = models.ForeignKey(Suppliers,on_delete=models.CASCADE)


class Cashier(models.Model):
    cashierID = models.IntegerField()
    employeeID =  models.ForeignKey(Employee,on_delete=models.CASCADE)
    stationStart = models.DateTimeField(auto_now_add=True) # confirm for auto_now_add
    stationEnd = models.DateTimeField(auto_now_add=True)
    


class Transactions(models.Model):
    transactionID = models.IntegerField()
    paymentMethod = models.CharField(max_length=10,default="cash")
    cashierID = models.ForeignKey(Cashier,on_delete=models.CASCADE)
    # paidAt = models.DateTimeField(auto_now_add=True) # confirm for auto_now_add and datetimefield
    # purchasedItems = models.CharField() list out the purchased items and relate them to their products id


class Sales(models.Model):
    # code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    noOfItems = models.IntegerField(default=0)
    paymentMethod = models.CharField(max_length=10,default="cash")
    # tax_amount = models.FloatField(default=0)
    # tax = models.FloatField(default=0)
    # tendered_amount = models.FloatField(default=0)
    # amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    # date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.grand_total)

