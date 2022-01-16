from django.urls import path
from . import views

app_name = 'isitchristmas'
urlpatterns = [
    path('', views.index, name= 'index'),
]

