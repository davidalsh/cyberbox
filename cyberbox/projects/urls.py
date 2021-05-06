from django.urls import path
from projects.views import ProjectsPageView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
]
