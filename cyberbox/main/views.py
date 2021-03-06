from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView

from main.forms import CreateUserForm, UserProfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import UserProfile
from projects.models import Projects, ApplyToProjectRequest


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'main/sign_up.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
        context = {
            'form': form,
        }
        return render(request, 'main/sign_up.html', context)


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'main/sign_in.html', {})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

        messages.info(request, 'Username or Password is incorrect.')

        context = {}
        return render(request, 'main/sign_in.html', context)


def SignOutView(request):
    logout(request)
    return redirect('home')


class ProfilePageView(LoginRequiredMixin, View):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request, username):
        if request.user.username == username:
            user = request.user
        else:
            user = get_object_or_404(User, username=username)

        try:
            about_user = UserProfile.objects.get(user_id=user.pk)
        except ObjectDoesNotExist:
            about_user = None

        try:
            user_projects = Projects.objects.filter(users=user)
        except ObjectDoesNotExist:
            user_projects = None

        context = {
            'profile_user': user,
            'about_user': about_user,
            'object_list': user_projects,
        }
        return render(request, 'main/profile.html', context)


class ProfilePageSettingsView(LoginRequiredMixin, View):  # Settings View
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request):
        try:
            user = UserProfile.objects.get(user_id=request.user.pk)
        except ObjectDoesNotExist:
            user = None

        if user:
            init_data = {
                'working_place': user.working_place,
                'about': user.about,
                'programming_languages': user.programming_languages.all(),
                'github': user.github,
                'linkedin': user.linkedin,
            }
        else:
            init_data = {}

        form = UserProfileForm(initial=init_data)

        context = {
            'form': form,
        }
        return render(request, 'main/settings.html', context)

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect('profile', username=request.user.username)

        context = {
            'form': form,
        }
        return render(request, 'main/settings.html', context)


class NotificationsView(LoginRequiredMixin, ListView):
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    model = Projects
    template_name = 'main/notifications.html'

    def get_queryset(self):
        queryset = ApplyToProjectRequest.objects.filter(project__owner_p=self.request.user)
        print(queryset)
        return queryset


class ProfileSettingsDeletePageView(LoginRequiredMixin, View):  # Delete View
    login_url = '/sign-in/'
    redirect_field_name = 'sign-in'

    def get(self, request):
        return render(request, 'main/delete_profile.html', {})

    def post(self, request):
        username = request.POST.get('username')

        if username == request.user.username:
            User.objects.get(id=request.user.id).delete()
            logout(request)
            return redirect('sign-up')

        messages.info(request, 'Username is incorrect.')

        context = {}
        return render(request, 'main/delete_profile.html', context)


class MainPageView(View):
    def get(self, request):
        return render(request, 'main/index.html')
