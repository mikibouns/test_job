from django.shortcuts import render


def sales_rate_page(request):
    template = "salesrate_app/salesrate.html"
    context = {}
    return render(request, template, context)