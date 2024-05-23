from django.urls import path, include
from .views import hello_dashboard


urlpatterns = [
    path('', hello_dashboard),
]