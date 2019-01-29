from django.db import models


class AdditionalServices(models.Model):
    as_name = models.CharField(verbose_name='name', max_length=32, blank=True, unique=True)

    def __str__(self):
        return self.as_name


class HotelCard(models.Model):
    hc_name = models.CharField(verbose_name='name', max_length=32, blank=True, unique=True, primary_key=True)
    hc_description = models.TextField(verbose_name='description', blank=True, null=True)
    hc_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')

    def __str__(self):
        return self.hc_name


class Category(models.Model):
    category_name = models.CharField(verbose_name='category', max_length=32, blank=True, unique=True)

    def __str__(self):
        return self.category_name


class HotelRoom(models.Model):
    hr_number = models.IntegerField(verbose_name='number', blank=True, unique=True, primary_key=True)
    hr_category = models.ForeignKey(Category)
    hr_description = models.TextField(verbose_name='description', blank=True, null=True)
    hr_price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)
    hr_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')
    hr_hotel = models.ForeignKey(HotelCard)

    def __str__(self):
        return self.hr_number









