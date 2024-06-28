from django.urls import path
from .views import upcoming_events, events_details
urlpatterns = [
    path('upcoming/', upcoming_events, name='upcoming_events'),
    path ('upcoming/<int:code>', events_details,name= 'events_details'),
]