from django.conf.urls import url
from . import views as catalog_views

urlpatterns = [
    url(r'', catalog_views.catalog_page, name='catalog_page'),
    url(r'(?P<hotel_card>\w+)/$', catalog_views.hotel_card_page, name='catalog_page'),
]