from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView

from projects.models import Projects
from projects.forms import CreateProjectForm


class ProjectsPageView(LoginRequiredMixin, ListView):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    model = Projects
    paginate_by = 16
    template_name = 'projects/projects.html'

    def get_queryset(self):
        queryset = Projects.objects.filter(open=True)
        return queryset


class CreateProjectView(LoginRequiredMixin, View):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request):
        form = CreateProjectForm()

        context = {
            'form': form,
        }
        return render(request, 'projects/create-project.html', context)

    def post(self, request):
        form = CreateProjectForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.project_owner = request.user
            obj.save()
            obj.users.add(request.user)
            form.save_m2m()
            return redirect('profile', username=request.user.username)

        context = {
            'form': form,
        }
        return render(request, 'projects/create-project.html', context)
