from django.urls import path
from . import views

urlpatterns = [
    path('theemail/', views.members, name='theemail'),
]