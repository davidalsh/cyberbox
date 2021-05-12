from django.urls import path
from projects.views import ProjectsPageView, CreateProjectView, ProjectEditView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('create/', CreateProjectView.as_view(), name='create-project'),
    path('project-edit/<int:project_id>/', ProjectEditView.as_view(), name='project-edit'),
]
