# Generated by Django 4.0.3 on 2022-04-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_remove_transactions_noofpurchaseditems_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='quantity',
        ),
        migrations.AddField(
            model_name='sales',
            name='noOfItems',
            field=models.IntegerField(default=0),
        ),
    ]
