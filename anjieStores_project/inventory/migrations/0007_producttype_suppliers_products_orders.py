# Generated by Django 4.0.3 on 2022-04-07 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_producttype_productsid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productTypeID', models.IntegerField()),
                ('productType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliersID', models.IntegerField()),
                ('suppliersName', models.CharField(max_length=25)),
                ('suppliersAddress', models.CharField(max_length=25)),
                ('suppliersContact', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productsID', models.IntegerField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=30)),
                ('Barcode', models.IntegerField()),
                ('ExpiryDate', models.DateField()),
                ('Price', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=35)),
                ('quantity', models.IntegerField()),
                ('productTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordersID', models.IntegerField()),
                ('orderDate', models.DateField()),
                ('qtyOrdered', models.IntegerField()),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.employee')),
                ('productsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.products')),
                ('suppliersID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.suppliers')),
            ],
        ),
    ]