import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # 部分一致

    class Meta:
        model = Product
        fields = ['name']