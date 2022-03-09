from django.db import models

# Create your models here.

# ProductsID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
# 					  ProductName VARCHAR(20) NOT NULL,
# 					  Barcode INT NOT NULL,
# 					  ExpiryDate DATE NOT NULL,
# 					  Price VARCHAR(15) NOT NULL,
# 					  SupplierID INT NOT NULL FOREIGN KEY REFERENCES Products(ProductsID),
# 					  OrdersID INT NOT NULL FOREIGN KEY REFERENCES Products(ProductsID),
# 					  ProductTypeID INT FOREIGN KEY REFERENCES Products(ProductsID))

# CREATE TABLE Employee(EmployeeID INT IDENTITY(1,1) UNIQUE,
# 					  FullName VARCHAR(35) NOT NULL,
# 					  Age INT NOT NULL,
# 					  DoB DATE NOT NULL,
# 					  Position VARCHAR(20),
# 					  PhoneNo VARCHAR(11) UNIQUE NOT NULL,
# 					  Address VARCHAR(50),
# 					  Status VARCHAR(10),
# 					  DateOfEmployment Date NOT NULL,
# 					  ShiftType VARCHAR(10) NOT NULL)

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

class Products(models.Model):
    productsID = models.IntegerField() #Primary key
    productName = models.CharField(max_length=30)
    Barcode = models.IntegerField()
    ExpiryDate = models.DateField()
    Price = models.IntegerField()
    supplierID = models.ForeignKey(Supplier)
    orderID = models.ForeignKey(Order)
    productTypeID=  models.ForeignKey(ProductType)

# CREATE TABLE Suppliers(SuppliersID INT IDENTITY(1,1) NOT NULL UNIQUE,
# 					   SuppliersName VARCHAR(25) NOT NULL,
# 					   SupAddress VARCHAR(25) NOT NULL,
# 					   SupPhoneNo VARCHAR(11) NOT NULL,
# 					   OrdersID INT NOT NULL,
# 					   ProductsID INT NOT NULL)

class Suppliers(models.Model):
    suppliersID = models.IntegerField()
    suppliersName = models.CharField(max_length=25)
    suppliersAddress = models.CharField(max_length=25)
    suppliersContact =models.CharField(max_length=11)
    ordersID = models.ForeignKey(Orders)

# CREATE TABLE Orders(OrdersID INT IDENTITY(1,1) NOT NULL,
# 					OrderDate DATE NOT NULL,
# 					QtyOrdered INT NOT NULL,
# 					ProductsID INT NOT NULL,
# 					EmployeeID INT NOT NULL,
# 					SuppliersID INT NOT NULL)

class Orders(models.Model):
    ordersID = models.IntegerField()
    orderDate = models.DateField()
    qtyOrdered = models.IntegerField()
    pro