# Generated by Django 4.0.3 on 2022-05-02 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_rename_productid_productsalesat_productsid'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsalesat',
            name='subTotal',
            field=models.IntegerField(default=0),
        ),
    ]
