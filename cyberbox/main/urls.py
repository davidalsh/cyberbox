from django.urls import path
from main.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('profile/<str:username>/', ProfilePageView.as_view(), name='profile'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-out/', SignOutView, name='sign-out'),
]
