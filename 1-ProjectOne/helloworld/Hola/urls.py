from django.urls import path
from . import views

# create your views

urlpatterns = [
    path('', views.homePageView, name='home'),
]