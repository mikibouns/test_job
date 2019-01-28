from django.conf.urls import url
from . import views as catalog_views

urlpatterns = [
    url(r'$', catalog_views.basic_page, name='basic_page'),
]