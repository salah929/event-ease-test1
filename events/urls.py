from django.urls import path
from . import views
from .views import EventCreateView, AboutView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('event/<slug:slug>/', views.EventDetails.as_view(),
         name='event_details'),
    path('', views.UpcomingEventList.as_view(), name='home'),
    path('past-events/', views.PastEventList.as_view(), name='past_events'),
]
