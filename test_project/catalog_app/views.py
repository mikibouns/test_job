from django.shortcuts import render
from .models import HotelCard, HotelRoom, ReservedDates
from django.db.models import Q


def catalog_page(request):
    hotel_cards = HotelCard.objects.all().order_by('pk')
    template = "catalog_app/catalog.html"
    context = {'hotels': hotel_cards}
    return render(request, template, context)


def hotel_card_page(request, pk):
    hotel_card = HotelCard.objects.get(id=pk)
    hotel_rooms = HotelRoom.objects.filter(hr_hotel__id=pk)
    check_in = (request.GET.get('check-in', None))
    check_out = (request.GET.get('check-out', None))
    places = (request.GET.get('places', None))
    filter = hotel_rooms
    if check_in and check_out and places:
        filter = hotel_rooms.filter(Q(hr_places=places) &
                                    (Q(reserveddates__check_in__lt=check_in) & Q(reserveddates__check_in__gt=check_out) |
                                         Q(reserveddates__check_out__gt=check_out) & Q(reserveddates__check_out__lt=check_in)))
        if request.method == 'POST':
            username = request.POST['additional_services']


    template = "catalog_app/hotel_card.html"
    context = {'hotel': hotel_card, 'rooms': hotel_rooms, 'room_filter': filter}
    return render(request, template, context)
