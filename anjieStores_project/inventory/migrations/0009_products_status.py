# Generated by Django 4.0.3 on 2022-04-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_itemcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]