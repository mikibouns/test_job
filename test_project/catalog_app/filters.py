from .models import HotelRoom
import django_filters


class RoomsFilter(django_filters.FilterSet):
    hr_places = django_filters.NumberFilter(field_name='hr_places', lookup_expr='lte')
    date_checkin = django_filters.DateFilter()
    date_checkout = django_filters.DateFilter()

    class Meta:
        model = HotelRoom
        fields = ['hr_places', 'date_checkin', 'date_checkout']
