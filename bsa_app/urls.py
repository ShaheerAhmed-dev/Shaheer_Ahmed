from django.urls import path
from .views import mechanical

urlpatterns = [
    path('mechanical/<str:equipment>', mechanical, name='mechanical'),
]
