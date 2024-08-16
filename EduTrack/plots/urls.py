from django.urls import path
from .views import read_data

app_name = 'plots'

urlpatterns = [
    path('read_data/', read_data, name='read_data'),
]