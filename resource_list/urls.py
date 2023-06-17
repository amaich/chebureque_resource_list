from django.urls import path
from .views import *

app_name = 'resource_list'

urlpatterns = [
    path('', tryer, name='tryer'),
]
