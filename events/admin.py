from django.contrib import admin
from .models import Event, EventRegistration
from .models import ContactMessage

# Register your models here.
admin.site.register(Event)
admin.site.register(EventRegistration)
admin.site.register(ContactMessage)
