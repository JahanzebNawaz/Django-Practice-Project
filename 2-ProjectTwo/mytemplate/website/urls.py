from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('navbar/', views.NavbarPageView.as_view(), name='navbar'),
]