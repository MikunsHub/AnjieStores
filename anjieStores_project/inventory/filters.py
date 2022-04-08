import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['Price','quantity','productsID','manufacturer']


class ProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ProductType
        fields = '__all__'
        exclude = ['productTypeID']