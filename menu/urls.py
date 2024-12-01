from django.urls import path
from . import views  


urlpatterns = [
    path('', views.home_view, name='home'),  
    path('philosophy/', views.philosophy_view, name='philosophy'),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('menu/', views.menu_view, name='menu'),
]
