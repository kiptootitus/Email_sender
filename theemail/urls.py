from django.urls import path
from . import views

urlpatterns = [
    path('theemail/', views.theemail, name='theemail'),
]