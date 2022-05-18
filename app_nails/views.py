from django.contrib import messages
from django.http.response import HttpResponseRedirect
from app_nails.models import Booking, PickDate
from django.http import request
from django.shortcuts import render
from app_nails.forms import BookingForm
import telepot
import random
from django.http import HttpResponse

token = '34625@361' # Your telegram bot's token
my_id = 123 # Your chat id with this bot
telegramBot = telepot.Bot(token)
def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")
# Create your views here.

def BookingView(request):
    
    form = BookingForm(request.POST)

    if form.is_valid():
        
        list = ['Вечер в хату 👊','Пламенный саламалейкум 🔥','Чики-брики в дамки 🤡','О,привет 👋','Привет,ну как там с деньгами? 💵','Бонжур 🥐','Девочка записалась на ноготочки 💅','Чупапи мунянё ✌','Салам БРО 😎','Цык-цык не спать на ✊','Держи краба 👊','Суету навести охото 🦁','Все, я погнал ✋','Пока что на расслабоне,на чилле.Кстати, у тебя новая запись 👇']
        form.save()
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        date_booking = form.cleaned_data['date_booking']
        message = str(random.choice(list)) + "\n" + "*К тебе записалась: *" +str(name) + "\n" + "*Вот её номер : *" + str(phone) + "\n" + "*Дата и время: *" + str(date_booking)
        send_message(message)
        return HttpResponseRedirect('thanks')
    else:
        messages.error(request, form.errors)
    context = {'form':form}
    return render(request,'appointment.html',context)

def Main(request):
    return render(request,'index.html')

def Thanks(request):
    return render(request,'thanks.html')