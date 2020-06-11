from django.urls import path 
from . import views

urlpatterns = [
    path('schedule', views.schedule, name='schedule'),
    path('speakers',views.speakers, name='speakers'),
    path('tickets', views.tickets, name='tickets'),
]
