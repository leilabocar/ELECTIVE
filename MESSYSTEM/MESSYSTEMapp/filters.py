from statistics import mode
import django_filters

from .models import *

class studentFilter(django_filters.FilterSet):
    class Meta:
        model = studentInfo
        fields = '__all__'
        