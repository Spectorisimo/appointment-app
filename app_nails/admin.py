from django.contrib import admin
from app_nails.models import Booking, PickDate
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','date_booking']

class PickAdmin(admin.ModelAdmin):
    list_display = ['date_booking']

admin.site.register(Booking,BookingAdmin)
admin.site.register(PickDate,PickAdmin)