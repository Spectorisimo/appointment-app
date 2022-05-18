from django.db import models

# Create your models here.
class PickDate(models.Model):
    date_booking = models.CharField(max_length=30,blank=True,verbose_name='Доступная дата посещения')
    def __str__(self):
         return f'{self.date_booking}'
    class Meta:
        verbose_name = "Доступная дата"
        verbose_name_plural = "Доступные даты"

class Booking(models.Model):
    name = models.CharField(max_length=30,blank=True,verbose_name='Имя:')
    phone = models.CharField(max_length=15,blank=False,verbose_name='Номер сотового телефона:')
    date_booking = models.OneToOneField(PickDate,blank=True,null=True,on_delete=models.CASCADE,unique=True,verbose_name='Дата посещения:')
    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"