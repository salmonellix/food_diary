from django.urls import path
from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('diary/', views.diary, name='diary'),
    path('day/<int:rid>', views.day, name='day')
]