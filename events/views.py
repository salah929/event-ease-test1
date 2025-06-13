from django.shortcuts import render
from django.views import generic
from .models import Event


class EventList(generic.ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(status=1)
    ordering = ['-created_at']
