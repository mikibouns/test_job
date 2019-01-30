from django.shortcuts import render
from .models import HotelCard, HotelRoom, AdditionalServices


def catalog_page(request):
    hotel_cards = HotelCard.objects.all().order_by('pk')
    template = "catalog_app/catalog.html"
    context = {'hotels': hotel_cards}
    return render(request, template, context)


def hotel_card_page(request, pk):
    hotel_card = HotelCard.objects.get(id=pk)
    hotel_rooms = HotelRoom.objects.filter(hr_hotel__id=pk)
    hotel_food = AdditionalServices.objects.all()
    template = "catalog_app/hotel_card.html"
    context = {'hotel': hotel_card, 'rooms': hotel_rooms, 'food': hotel_food}
    return render(request, template, context)
