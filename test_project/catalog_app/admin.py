from django.contrib import admin
from .models import HotelCard, Category, HotelRoom, ReservedDates


admin.site.register(Category)
admin.site.register(HotelCard)
admin.site.register(HotelRoom)
admin.site.register(ReservedDates)