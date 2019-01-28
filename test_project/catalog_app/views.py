from django.shortcuts import render, render_to_response


def basic_page(request):
    template = "base.html"
    context = {}
    return render(request, template, context)