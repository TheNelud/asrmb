import django_filters

from .models import *

class Losses_gas_apparatusFilter(django_filters.FilterSet):
    class Meta:
        model = Losses_gas_apparatus
        fields = '__all__'