from django.urls import path
from app_nails.views import BookingView, Main,Thanks
urlpatterns = [
    path('',Main,name='main'),
    path('appointment',BookingView,name='main'),
    path('thanks',Thanks,name='thanks'),

]