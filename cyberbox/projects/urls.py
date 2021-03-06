from django.urls import path
from projects.views import ProjectsPageView, CreateProjectView, ProjectEditView, DeleteProjectView, SearchResultView, \
    ProjectApplyView

urlpatterns = [
    path('', ProjectsPageView.as_view(), name='projects'),
    path('create/', CreateProjectView.as_view(), name='create-project'),
    path('project-edit/<int:project_id>/', ProjectEditView.as_view(), name='project-edit'),
    path('project-delete/<int:project_id>/', DeleteProjectView.as_view(), name='delete-project'),
    path('project-apply/<int:project_id>/', ProjectApplyView.as_view(), name='project-apply'),
    path('search/', SearchResultView.as_view(), name='search-results'),
]
