from django.contrib import admin
from .models import HotelCard, AdditionalServices, Category, HotelRoom

admin.site.register(Category)
admin.site.register(HotelCard)
admin.site.register(AdditionalServices)
admin.site.register(HotelRoom)