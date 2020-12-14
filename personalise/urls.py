from django.urls import path
from . import views

urlpatterns = [
    path('personalise/', views.personalise, name='personalise'),
]
