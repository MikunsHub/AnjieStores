# Generated by Django 4.0.3 on 2022-05-01 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_productsalesat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsalesat',
            old_name='productID',
            new_name='productsID',
        ),
    ]
