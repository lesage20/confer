from django.urls import path
from . import views

urlpatterns = [
    
   path('blog', views.blog, name='blog'),
   path('detail', views.detail, name='detail'),

]