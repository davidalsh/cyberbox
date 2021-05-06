from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView

from projects.models import Projects


class ProjectsPageView(LoginRequiredMixin, ListView):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    model = Projects
    paginate_by = 16
    template_name = 'projects/projects.html'

    def get_queryset(self):
        queryset = Projects.objects.filter(open=True)
        return queryset
