from django.urls import path
from .views import home, booking

urlpatterns = [
    path('', home, name='home'),
    path('result/', booking, name='bibliotheque')
]