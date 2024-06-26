from django.contrib.admin import register, ModelAdmin
from .models import Event

@register(Event)
class EventAdmin(ModelAdmin):
    pass