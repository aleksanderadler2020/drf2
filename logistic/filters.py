import django_filters

from logistic.models import Stock


class StockFilter(django_filters.FilterSet):
    products = django_filters.NumberFilter(field_name='products__id')

    class Meta:
        model = Stock
        fields = ['products']
