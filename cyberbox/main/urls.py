from django.urls import path
from main.views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
]
