from django.shortcuts import render


def main_page(request):
    template = "main_app/main.html"
    context = {}
    return render(request, template, context)
