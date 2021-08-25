import django_filters 
from .models import *
"""
   Filters  
"""

STATUS=(
        ('Available','Available'),
        ('Not Available','Not Available')
    )

class imgFilter(django_filters.FilterSet):
    # status = django_filters.Choice
    class Meta:
        model = Gallery
        fields = ['category']