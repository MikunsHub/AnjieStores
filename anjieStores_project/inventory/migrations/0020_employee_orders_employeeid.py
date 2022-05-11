# Generated by Django 4.0.3 on 2022-04-29 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0019_remove_orders_employeeid_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=35)),
                ('age', models.IntegerField()),
                ('doB', models.DateField()),
                ('position', models.CharField(max_length=20)),
                ('phoneNo', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=50)),
                ('stateOfOrigin', models.CharField(max_length=10)),
                ('employmentDate', models.DateField()),
                ('status', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='employeeID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.employee'),
            preserve_default=False,
        ),
    ]