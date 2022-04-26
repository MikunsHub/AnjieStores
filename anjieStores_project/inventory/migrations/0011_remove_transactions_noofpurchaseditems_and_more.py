# Generated by Django 4.0.3 on 2022-04-25 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_sales_delete_itemcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='noOfPurchasedItems',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='paidAt',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='totalAmount',
        ),
        migrations.AddField(
            model_name='sales',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='paymentMethod',
            field=models.CharField(default='cash', max_length=10),
        ),
    ]
