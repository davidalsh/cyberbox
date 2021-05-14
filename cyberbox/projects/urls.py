from django.urls import path
from projects.views import ProjectsPageView, CreateProjectView, ProjectEditView, DeleteProjectView, SearchResultView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('create/', CreateProjectView.as_view(), name='create-project'),
    path('project-edit/<int:project_id>/', ProjectEditView.as_view(), name='project-edit'),
    path('project-delete/<int:project_id>/', DeleteProjectView.as_view(), name='delete-project'),
    path('search/', SearchResultView.as_view(), name='search-results'),
]
