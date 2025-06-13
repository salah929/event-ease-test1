from django.shortcuts import render
from django.views import generic
from .models import Event
from datetime import date


class UpcomingEventList(generic.ListView):
    model = Event
    template_name = 'events/index.html'
    context_object_name = 'events'
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(status=1, date__gte=date.today()).order_by('date', 'time')


class PastEventList(generic.ListView):
    model = Event
    template_name = 'events/past_events.html'
    context_object_name = 'past_events'
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(status=1, date__lt=date.today()).order_by('-date', '-time')
