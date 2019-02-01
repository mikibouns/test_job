from django.db import models
from django.contrib.auth.models import User


class HotelCard(models.Model):
    hc_name = models.CharField(verbose_name='name', max_length=32, blank=True, unique=True)
    hc_description = models.TextField(verbose_name='description', blank=True, null=True)
    hc_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')

    def __str__(self):
        return str(self.hc_name)

    class Meta:
            ordering = ["id"]


class Category(models.Model):
    category_name = models.CharField(verbose_name='category', max_length=32, blank=True, unique=True)

    def __str__(self):
        return str(self.category_name)


class HotelRoom(models.Model):
    hr_places = models.DecimalField(verbose_name='places', max_digits=10, decimal_places=0)
    hr_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hr_description = models.TextField(verbose_name='description', blank=True, null=True)
    hr_price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)
    hr_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')
    hr_hotel = models.ForeignKey(HotelCard, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_reserved_dates(self):
        grd = ReservedDates.objects.filter(room=self.id)
        return grd

    class Meta:
            ordering = ["id"]


class ReservedDates(models.Model):
    user = models.ForeignKey(User)
    room = models.ForeignKey(HotelRoom)
    check_in = models.DateField(verbose_name='check-in')
    check_out = models.DateField(verbose_name='check-out')

    def __str__(self):
        return '{} > {}'.format(self.check_in, self.check_out)

    class Meta:
            ordering = ["room"]












