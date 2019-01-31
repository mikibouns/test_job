from django.shortcuts import render
from .models import HotelCard, HotelRoom
from .filters import RoomsFilter


def catalog_page(request):
    hotel_cards = HotelCard.objects.all().order_by('pk')
    template = "catalog_app/catalog.html"
    context = {'hotels': hotel_cards}
    return render(request, template, context)


def hotel_card_page(request, pk):
    hotel_card = HotelCard.objects.get(id=pk)
    hotel_rooms = HotelRoom.objects.filter(hr_hotel__id=pk)
    rooms_filter = RoomsFilter(request.GET, queryset=hotel_rooms)
    error = False
    if request.method == 'POST':
        check_in = request.POST['check-in']
        check_out = request.POST['check-out']
        number_of_beds = request.POST['places']
        print(check_in)
        print(check_out)
        print(number_of_beds)
    else:
        error = 'непрвильная дата'
    template = "catalog_app/hotel_card.html"
    context = {'hotel': hotel_card, 'rooms': hotel_rooms, 'filter': rooms_filter, 'error': error}
    return render(request, template, context)
