from django.contrib import admin
from .models import HotelCard, Category, HotelRoom, HotelDateRange


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["room", "__str__"]


admin.site.register(Category)
admin.site.register(HotelCard)
admin.site.register(HotelRoom)
admin.site.register(HotelDateRange, AuthorAdmin)