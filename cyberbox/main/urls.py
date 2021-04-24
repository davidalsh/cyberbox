from django.urls import path
from main.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
]
