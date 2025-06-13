from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpcomingEventList.as_view(), name='home'),
    path('past-events/', views.PastEventList.as_view(), name='past_events'),

]
