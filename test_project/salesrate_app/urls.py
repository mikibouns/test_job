from django.conf.urls import url
from . import views as sales_rate_views

urlpatterns = [
    url(r'$', sales_rate_views.sales_rate_page, name='sales_rate_page'),
]