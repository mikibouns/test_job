from django.conf.urls import url
from . import views as main_views

urlpatterns = [
    url(r'^$', main_views.main_page, name='main_page'),
]