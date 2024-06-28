from django.shortcuts import render
from .models import Event
from django.utils import timezone
from datetime import timedelta


def upcoming_events(request):
    now = timezone.now() 
    date = now - timedelta(days=7)
    data = Event.objects.filter(date__gt=date).order_by('-date')
    
    context = {
        'data' : data,
        'now' : now
    }
    return render(request,'upcoming_events.html', context)

def events_details(request, code):
    data = Event.objects.get(id=code)
    context = {
        'data' : data
    }
    return render (request, 'event_detail.html', context)