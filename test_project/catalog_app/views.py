from django.shortcuts import render


def catalog_page(request):
    template = "catalog_app/catalog.html"
    context = {}
    return render(request, template, context)


def hotel_card_page(request):
    template = "catalog_app/hotel_card.html"
    context = {}
    return render(request, template, context)