from django.shortcuts import render
from django.views import generic
from .models import Event, EventRegistration
from datetime import date
from .forms import EventRegistrationForm
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView
from django.shortcuts import redirect


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


class EventDetails(FormMixin, DetailView):
    model = Event
    template_name = "events/event_details.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    form_class = EventRegistrationForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        user = self.request.user
        context['form'] = EventRegistrationForm()
        context['registrations'] = EventRegistration.objects.filter(event=event)
        if user.is_authenticated:
            context['already_registered'] = EventRegistration.objects.filter(event=event, user=user).exists()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        event = self.object

        # Handle cancellation
        if request.POST.get("cancel_registration"):
            EventRegistration.objects.filter(event=event, user=request.user).delete()
            return redirect("event_details", slug=event.slug)

        # Handle new registration
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.user = request.user
            registration.save()
            return redirect("event_details", slug=event.slug)

        registrations = EventRegistration.objects.filter(event=event)
        is_registered = EventRegistration.objects.filter(event=event, user=request.user).exists()
        return render(
            request,
            "events/event_details.html",
            {
                "event": event,
                "form": form,
                "registrations": registrations,
                "is_registered": is_registered,
            },
        )
