from django.db import models


class HotelCard(models.Model):
    hc_name = models.CharField(verbose_name='name', max_length=32, blank=True, unique=True)
    hc_description = models.TextField(verbose_name='description', blank=True, null=True)
    hc_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')

    def __str__(self):
        return str(self.hc_name)


class Category(models.Model):
    category_name = models.CharField(verbose_name='category', max_length=32, blank=True, unique=True)

    def __str__(self):
        return str(self.category_name)


class HotelRoom(models.Model):
    hr_places = models.DecimalField(verbose_name='places', max_digits=10, decimal_places=0)
    hr_category = models.ForeignKey(Category)
    hr_description = models.TextField(verbose_name='description', blank=True, null=True)
    hr_price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)
    hr_title_img = models.ImageField(verbose_name='title_img', blank=True, upload_to='media')
    hr_hotel = models.ForeignKey(HotelCard)

    def __str__(self):
        return str(self.id)

    def get_date_range(self):
        date_range = HotelDateRange.objects.filter(room=self.id)
        return date_range


class HotelDateRange(models.Model):
    room = models.ForeignKey(HotelRoom)
    checkin = models.DateField(verbose_name='check-in')
    checkout = models.DateField(verbose_name='check-out')

    def __str__(self):
        return '{} > {}'.format(self.checkin, self.checkout)












