from django.urls import path
from .views import LandingViewSet

urlpatterns = [
    path('landing/', LandingViewSet.as_view(), name='landing')
]