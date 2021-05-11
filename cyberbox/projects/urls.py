from django.urls import path
from projects.views import ProjectsPageView, CreateProjectView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('create/', CreateProjectView.as_view(), name='create-project'),
]
