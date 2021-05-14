from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView

from django.contrib import messages
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


class ProjectEditView(LoginRequiredMixin, View):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request, project_id):
        project = get_object_or_404(Projects, pk=project_id)

        if project.project_owner != request.user:
            return HttpResponseForbidden()

        form = CreateProjectForm(instance=project)

        context = {
            'form': form,
            'projectid': project_id,
        }

        return render(request, 'projects/edit-project.html', context)

    def post(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)

        if project.project_owner != request.user:
            return HttpResponseForbidden()

        form = CreateProjectForm(request.POST, instance=project)

        if form.is_valid():
            project.title = request.POST.get('title')
            project.description = request.POST.get('description')
            project.open = True if request.POST.get('open') else False
            project.max_members = request.POST.get('max_members')
            project.save()

            project.programming_languages_are_using.set(request.POST.getlist('programming_languages_are_using'))
            project.searching_for_working_place.set(request.POST.getlist('searching_for_working_place'))

            return redirect('profile', username=request.user.username)

        context = {
            'form': form,
            'projectid': project_id,
        }

        return render(request, 'projects/edit-project.html', context)


class DeleteProjectView(LoginRequiredMixin, View):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request, project_id):
        project = get_object_or_404(Projects, pk=project_id)

        if project.project_owner != request.user:
            return HttpResponseForbidden()

        context = {
            'project': project,
        }
        return render(request, 'projects/delete-project.html', context)

    def post(self, request, project_id):
        project = get_object_or_404(Projects, id=project_id)

        if project.project_owner != request.user:
            return HttpResponseForbidden()

        if int(request.POST.get('project_id')) == project_id:
            project.delete()
            return redirect('profile', username=request.user.username)

        messages.info(request, 'Project ID is incorrect.')

        context = {
            'project': project,
        }

        return render(request, 'projects/delete-project.html', context)


class SearchResultView(LoginRequiredMixin, ListView):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    model = Projects
    paginate_by = 16
    template_name = 'projects/projects.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if not query:
            return Projects.objects.filter(open=True)

        if query[0] == '#':

            project_id = query.replace('#', '')

            if not project_id.isdigit():
                return Projects.objects.filter(title__icontains=query)

            object_list = Projects.objects.filter(id=project_id)

        else:
            object_list = Projects.objects.filter(title__icontains=query)

        return object_list

