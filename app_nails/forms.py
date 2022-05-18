from app_nails.models import Booking,PickDate
from django import forms
from django.contrib import messages


class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['phone'].required = True
        self.fields['date_booking'].required = True
    class Meta:
        model = Booking
        fields = ['name','phone','date_booking']
        error_messages = {
                'date_booking': {
                    'unique': ("Выбранная Вами запись уже занята."),
                },


            }   
