from .models import HotelRoom
import django_filters


class RoomsFilter(django_filters.FilterSet):
    date_range = django_filters.DateRangeFilter()
    hr_places = django_filters.NumberFilter(field_name='hr_places', lookup_expr='lte')

    class Meta:
        model = HotelRoom
        fields = ['date_range', 'hr_places']
