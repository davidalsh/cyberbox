from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from main.views import MainPageView, ProfilePageView, SignInView, SignUpView, SignOutView, ProfilePageSettingsView

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('profile/<str:username>/', ProfilePageView.as_view(), name='profile'),
    path('settings/profile/', ProfilePageSettingsView.as_view(), name='profile-settings'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-out/', SignOutView, name='sign-out'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
