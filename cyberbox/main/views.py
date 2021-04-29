from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.core.exceptions import ObjectDoesNotExist


from main.forms import CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import UserProfile


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
        user = get_object_or_404(User, username=username)
        try:
            userprofile = UserProfile.objects.get(user_id=user.pk)
        except ObjectDoesNotExist:
            userprofile = None
        print(userprofile)
        context = {
            'profile_user': user,
            'about_user': userprofile,
        }
        return render(request, 'main/profile.html', context)


class MainPageView(View):
    def get(self, request):
        return render(request, 'main/index.html')
