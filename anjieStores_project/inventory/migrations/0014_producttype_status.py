# Generated by Django 4.0.3 on 2022-04-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_sales_paymentmethod'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]