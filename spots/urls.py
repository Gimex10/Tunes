from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_music/', views.addMusic, name="add_music"),
]
