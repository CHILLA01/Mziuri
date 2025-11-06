
from django.urls import path
from . import views

urlpatterns = [
    path('mziuri', views.my_name, name='mziuri'),
]
