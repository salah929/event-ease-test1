from django.urls import path
from . import views

urlpatterns = [
    path('event/<slug:slug>/', views.EventDetails.as_view(),
         name='event_details'),
    path('', views.UpcomingEventList.as_view(), name='home'),
    path('past-events/', views.PastEventList.as_view(), name='past_events'),

]
