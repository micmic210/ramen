from django.urls import path
from .views import reservation_view

urlpatterns = [
    path('reservation/', reservation_view, name='reservation'), 
]
