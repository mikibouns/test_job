from django.shortcuts import render
from .models import HotelCard, HotelRoom, AdditionalServices, Category

hotel_cards = HotelCard.objects.all()


def catalog_page(request):
    template = "catalog_app/catalog.html"
    context = {'hotels': hotel_cards}
    return render(request, template, context)


def hotel_card_page(request, pk):
    print(pk)
    template = "catalog_app/hotel_card.html"
    context = {}
    return render(request, template, context)